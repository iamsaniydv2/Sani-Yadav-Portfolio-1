from django.shortcuts import render, redirect
from django.db import models
from django.contrib import admin
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from .models import Profile, Resume, Portfolio, Summary, Education, Contact

# HOME
def index(request):
    smry=Summary.objects.all()
    education=Education.objects.all()
    
    
    profile_data = Profile.objects.values()
    context={'smry':smry,'profile': profile_data,'education':education}
    print(profile_data)
    return render(request, 'index.html',context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('user_name')    
        email = request.POST.get('user_email')  
        phone = request.POST.get('phone')  
        message = request.POST.get('message')

        try:
            # Save to database
            contact = Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
            )

            try:
                # Send email to admin
                admin_email_sent = send_mail(
                    subject=f"New Contact Form Submission - {name}",
                    message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                print(f"Admin email sent: {admin_email_sent}")
                
                # Send confirmation to user
                user_email_sent = send_mail(
                    subject=f"Thank you for contacting us, {name}!",
                    message=f"Hello {name},\n\nThank you for your message. We have received it successfully.\n\nWe will get back to you soon.\n\nBest regards,\nSani Yadav",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                )
                print(f"User email sent: {user_email_sent}")
                
                messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
                return redirect('index_html')

            except Exception as e:
                print(f"Error sending email: {e}")
                messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
                return redirect('index_html')

        except Exception as e:
            print(f"Error saving contact: {e}")
            messages.error(request, 'There was an error submitting the form. Please try again.')
            return redirect('index_html')

    return redirect('index_html' + '#contact')


# ABOUT US
def about_us(request):
    about_data = Profile.objects.all()  # Using Profile model instead of AboutUs
    return render(request, 'about_us.html', {'about': about_data})

# RESUME 
def resume(request):
    resume = Resume.objects.values()
    print(resume)
    return render(request, 'resume.html', {'resume': resume})


# SERVICES 
def services(request):
    services_list = [
        {"title": "Web Development", "description": "Custom website development using modern technologies."},
        {"title": "Python/Django", "description": "Backend development with Python and Django framework."},
        {"title": "Frontend Development", "description": "Responsive and interactive frontend development."},
    ]
    return render(request, 'services.html', {'services': services_list})
    

# PORTFOLIO 
def portfolio(request):
    portfolio = Portfolio.objects.values()
    print(portfolio)
    return render(request,'portfolio.html', {'portfolio': portfolio})

# PORTFOLIO DETAILS 
def portfolio_details(request):
    return render(request, 'portfolio-details.html')

# JOB PAGE
def job(request):
    return render(request, 'job.html')

# PROJECT 2 PAGE
def project2(request):
    return render(request, 'project2.html')

# PROJECT 04 PAGE
def project04(request):
    return render(request, 'project04.html')

# PROJECT4
def project4(request):
    return render(request, 'project4.html')

# SERVICE DETAILS PAGE
def service_details(request):
    service = request.GET.get('service', 'web') 
    context = {
        'service': service
    }
    return render(request, 'service-details.html', context)

# SKILLS PAGE
def skills(request):
    return render(request, 'skills.html')

# PROJECT05
def project05(request):
    return render(request, 'project05.html')

# PROJECT 06 PAGE
def project06(request):
    return render(request, 'project06.html')

# QUICKSUPPORT PAGE
def quicksupport(request):
    return render(request, 'quicksupport.html')

