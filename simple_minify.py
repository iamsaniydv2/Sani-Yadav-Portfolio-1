import os
import glob

def minify_css():
    """Minify CSS files in the static directory"""
    print("🔍 Searching for CSS files...")
    
    # Find all CSS files in static directory
    css_files = glob.glob('portfolio/static/**/*.css', recursive=True)
    
    for css_file in css_files:
        # Skip already minified files
        if '.min.css' in css_file:
            continue
            
        try:
            # Read original file
            with open(css_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple minification (remove comments and extra whitespace)
            minified = ' '.join(content.split())
            minified = minified.replace('{ ', '{').replace(' }', '}')
            minified = minified.replace('; ', ';').replace(': ', ':')
            
            # Save minified version
            min_file = css_file.replace('.css', '.min.css')
            with open(min_file, 'w', encoding='utf-8') as f:
                f.write(minified)
                
            print(f"✅ Minified: {os.path.basename(css_file)}")
            
        except Exception as e:
            print(f"❌ Error processing {css_file}: {str(e)}")

def minify_js():
    """Minify JS files in the static directory"""
    print("\n🔍 Searching for JS files...")
    
    # Find all JS files in static directory
    js_files = glob.glob('portfolio/static/**/*.js', recursive=True)
    
    for js_file in js_files:
        # Skip already minified files and node_modules
        if '.min.js' in js_file or 'node_modules' in js_file:
            continue
            
        try:
            # Read original file
            with open(js_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple minification (remove comments and extra whitespace)
            minified = ' '.join(content.split())
            
            # Save minified version
            min_file = js_file.replace('.js', '.min.js')
            with open(min_file, 'w', encoding='utf-8') as f:
                f.write(minified)
                
            print(f"✅ Minified: {os.path.basename(js_file)}")
            
        except Exception as e:
            print(f"❌ Error processing {js_file}: {str(e)}")

def update_html():
    """Update HTML files to use minified CSS/JS"""
    print("\n🔄 Updating HTML files...")
    
    # Find all HTML files in templates directory
    html_files = glob.glob('portfolio/templates/**/*.html', recursive=True)
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            updated = False
            
            # Update CSS links
            if '.css"' in content and not '.min.css' in content:
                content = content.replace('.css"', '.min.css"')
                updated = True
                
            # Update JS scripts
            if '.js"' in content and not '.min.js' in content:
                content = content.replace('.js"', '.min.js"')
                updated = True
            
            if updated:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Updated: {os.path.basename(html_file)}")
                
        except Exception as e:
            print(f"❌ Error updating {html_file}: {str(e)}")

if __name__ == "__main__":
    print("🚀 Starting asset optimization...")
    minify_css()
    minify_js()
    update_html()
    print("\n✨ Asset optimization completed!")
