import os
import sys
import glob
import subprocess
import time

def install_package(package):
    print(f"Installing {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from csscompressor import compress as css_compress
except ImportError:
    install_package('csscompressor')
    from csscompressor import compress as css_compress

try:
    from rjsmin import jsmin
except ImportError:
    install_package('rjsmin')
    from rjsmin import jsmin

def find_files(directory, extensions):
    """Find all files with given extensions in directory"""
    file_list = []
    for ext in extensions:
        file_list.extend(glob.glob(f"{directory}/**/*{ext}", recursive=True))
    return file_list

def minify_css():
    print("\n🔍 Searching for CSS files...")
    css_files = find_files('portfolio/static', ['.css'])
    
    # Exclude already minified files
    css_files = [f for f in css_files if not f.endswith('.min.css')]
    
    if not css_files:
        print("No CSS files found to minify.")
        return
        
    print(f"Found {len(css_files)} CSS files to minify.")
    
    for css_file in css_files:
        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                css_content = f.read()
            
            # Get file stats before minification
            original_size = os.path.getsize(css_file)
            
            # Minify CSS
            minified_css = css_compress(css_content)
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(min_file), exist_ok=True)
            
            # Save minified CSS with .min.css extension
            min_file = css_file.replace('.css', '.min.css')
            with open(min_file, 'w', encoding='utf-8') as f:
                f.write(minified_css)
                
            # Get file stats after minification
            minified_size = os.path.getsize(min_file)
            savings = original_size - minified_size
            savings_percent = (savings / original_size) * 100
            
            print(f"✅ Minified: {os.path.basename(css_file):<30} {original_size/1024:6.1f} KB → {minified_size/1024:5.1f} KB (Saved: {savings/1024:.1f} KB, {savings_percent:.1f}%)")
            
        except Exception as e:
            print(f"❌ Error minifying {css_file}: {str(e)}")

def minify_js():
    print("\n🔍 Searching for JS files...")
    js_files = find_files('portfolio/static', ['.js'])
    
    # Exclude already minified files and node_modules
    js_files = [f for f in js_files 
               if not f.endswith('.min.js') 
               and 'node_modules' not in f]
    
    if not js_files:
        print("No JS files found to minify.")
        return
        
    print(f"Found {len(js_files)} JS files to minify.")
    
    for js_file in js_files:
        try:
            with open(js_file, 'r', encoding='utf-8') as f:
                js_content = f.read()
            
            # Get file stats before minification
            original_size = os.path.getsize(js_file)
            
            # Minify JS
            minified_js = jsmin(js_content)
            
            # Save minified JS with .min.js extension
            min_file = js_file.replace('.js', '.min.js')
            with open(min_file, 'w', encoding='utf-8') as f:
                f.write(minified_js)
            
            # Get file stats after minification
            minified_size = os.path.getsize(min_file)
            savings = original_size - minified_size
            savings_percent = (savings / original_size) * 100
            
            print(f"✅ Minified: {os.path.basename(js_file):<30} {original_size/1024:6.1f} KB → {minified_size/1024:5.1f} KB (Saved: {savings/1024:.1f} KB, {savings_percent:.1f}%)")
            
        except Exception as e:
            print(f"❌ Error minifying {js_file}: {str(e)}")

def update_html_templates():
    """Update HTML templates to use minified CSS/JS"""
    print("\n🔄 Updating HTML templates...")
    
    # Find all HTML files
    html_files = find_files('portfolio/templates', ['.html'])
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace .css with .min.css and .js with .min.js
            updated = False
            
            # Update CSS links
            if '.css' in content and not '.min.css' in content:
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

def main():
    print("🚀 Starting asset optimization...")
    start_time = time.time()
    
    try:
        # Create minified versions
        minify_css()
        minify_js()
        
        # Update HTML templates to use minified files
        update_html_templates()
        
        # Calculate and display total time
        total_time = time.time() - start_time
        print(f"\n✨ Asset optimization completed in {total_time:.2f} seconds!")
        
    except Exception as e:
        print(f"\n❌ Error during optimization: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
