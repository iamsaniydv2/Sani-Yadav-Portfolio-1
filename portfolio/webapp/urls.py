from django.urls import path
from .views import index, contact, about_us, services, portfolio, resume, portfolio_details
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('resume/', resume, name='resume'),
    path('contact/', contact, name='contact'),
    path('about_us/', about_us, name='about'),
    path('skills/', views.skills, name='skills'),
    path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio-details.html', portfolio_details, name='portfolio_details'),
    path('quicksupport.html', views.quicksupport, name='quicksupport'),
    path('project2.html', views.project2, name='project2'),
    path('project04.html', views.project04, name='project04'),
    path('project4.html', views.project4, name='project4'),
    path('project05.html', views.project05, name='project05'),
    path('project06.html', views.project06, name='project06'),
    # Service details with both .html and without, with and without trailing slash
    path('service-details/', views.service_details, name='service_details'),
    path('service-details', views.service_details, name='service_details_no_slash'),
    path('service-details.html', views.service_details, name='service_details_html'),
    path('job.html', views.job, name='job'),
    path('index.html', index, name='index_html')
]
  


