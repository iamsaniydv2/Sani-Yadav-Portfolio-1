import os
from PIL import Image
from pathlib import Path

def optimize_remaining_images():
    # Define paths
    img_dir = os.path.join('portfolio', 'static', 'img')
    optimized_dir = os.path.join(img_dir, 'optimized')
    os.makedirs(optimized_dir, exist_ok=True)
    
    # Supported image formats
    img_formats = ('.jpg', '.jpeg', '.png')
    
    # Process each image
    for root, _, files in os.walk(img_dir):
        # Skip the optimized directory to avoid re-processing
        if 'optimized' in root and root != optimized_dir:
            continue
            
        for file in files:
            if file.lower().endswith(img_formats) and not file.lower().endswith('.webp'):
                try:
                    img_path = os.path.join(root, file)
                    rel_path = os.path.relpath(img_path, img_dir)
                    output_path = os.path.join(optimized_dir, os.path.splitext(rel_path)[0] + '.webp')
                    
                    # Skip if already optimized
                    if os.path.exists(output_path):
                        continue
                        
                    # Create output directory structure
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    
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
                    
                    print(f"Optimized: {file} -> {os.path.relpath(output_path, img_dir)}")
                    
                except Exception as e:
                    print(f"Error optimizing {file}: {str(e)}")

if __name__ == "__main__":
    print("Starting image optimization...")
    optimize_remaining_images()
    print("Image optimization completed!")
