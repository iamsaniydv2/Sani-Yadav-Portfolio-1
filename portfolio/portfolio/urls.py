"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sites.models import Site
from webapp import views
from webapp.sitemap import StaticViewSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

# Ensure the default site is set correctly
from django.contrib.sites.shortcuts import get_current_site

# Sitemap configuration
sitemaps = {
    'static': StaticViewSitemap,
}

# Get the current site
try:
    site = get_current_site(None)
    SITE_DOMAIN = site.domain
    SITE_NAME = site.name
    SITE_ID = site.id
except:
    SITE_DOMAIN = 'sani-yadav-portfolio-9.onrender.com'
    SITE_NAME = 'Sani Yadav Portfolio'
    SITE_ID = 1

# Update the site domain if needed
if not settings.DEBUG:
    from django.contrib.sites.models import Site
    Site.objects.update_or_create(
        id=SITE_ID,
        defaults={
            'domain': SITE_DOMAIN,
            'name': SITE_NAME
        }
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('project4.html', views.project4, name='project4'),
    
    # Sitemap URL with proper configuration
    path('sitemap.xml', sitemap, 
        {'sitemaps': sitemaps, 'template_name': 'sitemap.xml'}, 
        name='django.contrib.sitemaps.views.sitemap'
    ),
    
    # Robots.txt with template view for better control
    path('robots.txt', TemplateView.as_view(
        template_name='robots.txt', 
        content_type='text/plain'
    ), name='robots_file'),
]

# For serving static files in development and production
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

def project4(request):
    return render(request, 'project4.html')
