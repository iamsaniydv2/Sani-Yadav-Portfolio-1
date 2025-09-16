import os
from PIL import Image
from pathlib import Path

def optimize_images():
    """
    Optimize images by converting them to WebP and JPG formats in multiple sizes.
    Creates optimized versions in the 'optimized' directory.
    """
    # Define paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, 'portfolio', 'static')
    img_dir = os.path.join(static_dir, 'img')
    
    # Create optimized directory if it doesn't exist
    optimized_dir = os.path.join(static_dir, 'img', 'optimized')
    os.makedirs(optimized_dir, exist_ok=True)
    
    # Supported input image formats
    img_formats = ('.jpg', '.jpeg', '.png', '.webp')
    
    # Define output sizes (width, height)
    sizes = [
        (400, 225),  # Small
        (800, 450),  # Medium
        (1200, 675)  # Large
    ]
    
    # Process each image
    for root, _, files in os.walk(img_dir):
        # Skip the optimized directory to prevent reprocessing
        if 'optimized' in root:
            continue
            
        for file in files:
            if file.lower().endswith(img_formats):
                try:
                    img_path = os.path.join(root, file)
                    rel_path = os.path.relpath(img_path, img_dir)
                    output_path = os.path.join(optimized_dir, os.path.splitext(rel_path)[0] + '.webp')
                    
                    # Create output directory structure
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    
                    # Get original dimensions
                    orig_width, orig_height = img.size
                    
                    # Process each size
                    for width, height in sizes:
                        # Create output filenames
                        filename = os.path.splitext(file)[0]
                        
                        # Resize image maintaining aspect ratio
                        ratio = min(width/orig_width, height/orig_height)
                        new_width = int(orig_width * ratio)
                        new_height = int(orig_height * ratio)
                        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                        
                        # Save as WebP
                        webp_filename = f"{filename}-{width}x{height}.webp"
                        webp_path = os.path.join(optimized_dir, webp_filename)
                        resized_img.save(webp_path, 'webp', quality=85, optimize=True)
                        
                        # Save as JPG (fallback)
                        jpg_filename = f"{filename}-{width}x{height}.jpg"
                        jpg_path = os.path.join(optimized_dir, jpg_filename)
                        resized_img.save(jpg_path, 'JPEG', quality=85, optimize=True)
                        
                        print(f"Created: {webp_filename}, {jpg_filename}")
                    
                    print(f"Processed: {file}")
                    
                except Exception as e:
                    print(f"Error processing {file}: {str(e)}")
                    import traceback
                    traceback.print_exc()

if __name__ == "__main__":
    print("Starting image optimization...")
    optimize_images()
    print("Image optimization completed!")
