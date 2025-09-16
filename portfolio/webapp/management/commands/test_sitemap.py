from django.core.management.base import BaseCommand
from django.urls import reverse
from django.contrib.sites.models import Site
from webapp.sitemap import StaticViewSitemap

class Command(BaseCommand):
    help = 'Test the sitemap generation'

    def handle(self, *args, **options):
        # Set the site domain for testing
        site = Site.objects.get_current()
        self.stdout.write(f"Current site: {site.domain}")
        
        # Test sitemap generation
        sitemap = StaticViewSitemap()
        urls = sitemap.get_urls()
        
        self.stdout.write("\nSitemap URLs:")
        self.stdout.write("-" * 80)
        for url in urls:
            self.stdout.write(f"URL: {url['location']}")
            self.stdout.write(f"Last modified: {url.get('lastmod', 'Not specified')}")
            self.stdout.write(f"Change frequency: {url.get('changefreq', 'weekly')}")
            self.stdout.write(f"Priority: {url.get('priority', '0.5')}")
            self.stdout.write("-" * 80)
            
        self.stdout.write("\nTo view the sitemap, visit:")
        self.stdout.write("https://sani-yadav-portfolio-9.onrender.com/sitemap.xml")
