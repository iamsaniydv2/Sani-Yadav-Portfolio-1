import os
import re
from bs4 import BeautifulSoup
from pathlib import Path

def get_project_root():
    """Get the root directory of the project."""
    return os.path.dirname(os.path.abspath(__file__))

def update_image_tags(html_file):
    project_root = get_project_root()
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    modified = False
    
    # Update all img tags
    for img in soup.find_all('img'):
        src = img.get('src', '')
        
        # Skip if already using WebP or no src
        if not src or '.webp' in src.lower() or not ('static' in src or 'img' in src):
            continue
            
        # Extract image path from Django template tag
        if '{%' in src and '%}' in src:
            # Handle Django template tags
            img_path = src.split("'")[1]  # Extract path from {% static 'path/to/img.jpg' %}
            webp_path = img_path.rsplit('.', 1)[0] + '.webp'
            webp_static_path = os.path.join(project_root, 'portfolio', 'static', webp_path)
            
            if os.path.exists(webp_static_path):
                # Update src to use WebP
                new_src = "{% static '" + webp_path + "' %}"
                img['src'] = new_src
                
                # Add loading="lazy" if not present
                if not img.get('loading'):
                    img['loading'] = 'lazy'
                    
                # Add width and height if missing
                if not img.get('width') or not img.get('height'):
                    try:
                        from PIL import Image
                        img_file = os.path.join(project_root, 'portfolio', 'static', img_path)
                        with Image.open(img_file) as img_file_obj:
                            width, height = img_file_obj.size
                            img['width'] = str(width)
                            img['height'] = str(height)
                    except Exception as e:
                        print(f"Warning: Could not get dimensions for {img_path}: {e}")
                
                print(f"Updated image: {img_path} -> {webp_path}")
                modified = True
    
    # Save changes if any modifications were made
    if modified:
        with open(html_file, 'w', encoding='utf-8', newline='\n') as f:
            f.write(str(soup))
        print(f"✅ Updated: {os.path.basename(html_file)}")
    else:
        print(f"ℹ️  No changes needed: {os.path.basename(html_file)}")

def main():
    print("🚀 Starting image tag updates...")
    project_root = get_project_root()
    templates_dir = os.path.join(project_root, 'portfolio', 'templates')
    
    if not os.path.exists(templates_dir):
        print(f"❌ Error: Templates directory not found at {templates_dir}")
        return
    
    # Process all HTML files in the templates directory
    for root, _, files in os.walk(templates_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                print(f"\n📄 Processing: {file}" + "-"*50)
                update_image_tags(file_path)

if __name__ == "__main__":
    main()
    print("\n✨ Image tag updates completed!")
