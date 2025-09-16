import os
from PIL import Image

def optimize_image():
    # Define paths
    static_dir = os.path.join('portfolio', 'static')
    img_path = os.path.join(static_dir, 'img', 'services.jpg')
    output_dir = os.path.join(static_dir, 'img', 'optimized')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'services.webp')
    
    try:
        # Open and optimize image
        with Image.open(img_path) as img:
            # Convert to RGB if RGBA
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Calculate new dimensions (max 1200px width, maintain aspect ratio)
            max_size = (1200, 1200)
            img.thumbnail(max_size, Image.LANCZOS)
            
            # Save as WebP with 80% quality
            img.save(
                output_path,
                'WEBP',
                quality=80,
                optimize=True,
                method=6  # Best quality encoding
            )
        
        print(f"✅ Image optimized and saved as: {output_path}")
        print(f"Original size: {os.path.getsize(img_path) / 1024:.2f} KB")
        print(f"Optimized size: {os.path.getsize(output_path) / 1024:.2f} KB")
        
        # Update HTML to use the optimized image
        update_html()
        
    except Exception as e:
        print(f"❌ Error optimizing image: {str(e)}")

def update_html():
    html_file = os.path.join('portfolio', 'templates', 'service-details.html')
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the image source with WebP version
        new_content = content.replace(
            'img/services.jpg"',
            'img/optimized/services.webp" width="800" height="500" loading="lazy"'
        )
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ HTML updated to use optimized WebP image")
        
    except Exception as e:
        print(f"❌ Error updating HTML: {str(e)}")

if __name__ == "__main__":
    print("🔄 Optimizing services image...")
    optimize_image()
    print("✨ Optimization process completed!")
