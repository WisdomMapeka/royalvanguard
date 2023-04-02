from django.shortcuts import render
from . models import (Contacts_Plus_Social_Media, Slider, SummaryServices, 
                      AboutUs, Services, WhyChooseUsSummary, OurProjects, 
                      TeamMembers, Testimonials, ContactUs, BackGroundImages, Sectors)
from . forms import ContactUsForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

def index(request):
    b = BackGroundImages.objects.all()[0]
    sectors = Sectors.objects.all()
    try:
        contact_details = Contacts_Plus_Social_Media.objects.all()[0]
    except IndexError:
        contact_details = False
    
    slider = Slider.objects.all()
    service_summaries = SummaryServices.objects.all()
    services = Services.objects.all()
    projects = OurProjects.objects.all()
    teammembers = TeamMembers.objects.all()
    testimonials = Testimonials.objects.all()
    try:
        whychooseus = WhyChooseUsSummary.objects.all()[0]
    except IndexError:
        whychooseus = False
    
    try:
        about_us = AboutUs.objects.all()[0]
    except IndexError:
        about_us = False

    
    
    return render(request, "main/index.html", {"contact_details":contact_details,
                                               "slider":slider,
                                               "service_summaries":service_summaries,
                                               "about_us":about_us, 
                                               "services":services,
                                               "whychooseus":whychooseus,
                                               "projects":projects,
                                               "teammembers":teammembers,
                                               "testimonials":testimonials,
                                               "b":b,
                                               "sectors":sectors
                                               })


def about(request):
    try:
        contact_details = Contacts_Plus_Social_Media.objects.all()[0]
    except IndexError:
        contact_details = False

    try:
        about_us = AboutUs.objects.all()[0]
    except IndexError:
        about_us = False

    teammembers = TeamMembers.objects.all()
    services = Services.objects.all()

    return render(request, "main/about.html", {"contact_details":contact_details,
                                               "about_us":about_us,
                                               "teammembers":teammembers,
                                               "services":services })

def services(request):
    try:
        contact_details = Contacts_Plus_Social_Media.objects.all()[0]
    except IndexError:
        contact_details = False

    services = Services.objects.all()

    return render(request, "main/service.html", {"contact_details":contact_details,
                                                 "services":services,})


def projects(request):
    try:
        contact_details = Contacts_Plus_Social_Media.objects.all()[0]
    except IndexError:
        contact_details = False

    services = Services.objects.all()
    projects = OurProjects.objects.all()

    return render(request, "main/project.html", {"contact_details":contact_details,
                                                 "services":services,
                                                 "projects":projects,})

                    
def contacts(request):
    try:
        contact_details = Contacts_Plus_Social_Media.objects.all()[0]
    except IndexError:
        contact_details = False

    services = Services.objects.all()
    projects = OurProjects.objects.all()

    form = ContactUsForm()
    
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print(request.POST['name'])
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            saving = ContactUs(name=name, email=email, phone=phone, subject=subject, message=message)
            saving.save()
            return HttpResponseRedirect('/thanks/')
          
        else:
            print(form.errors)
            form = ContactUsForm(request.POST)
            messages.add_message(request, messages.INFO, form.errors)
 

    return render(request, "main/contact.html", {"contact_details":contact_details,
                                                 "services":services,
                                                 "projects":projects,
                                                 "form":form})


def sending_message_form_success(request):
    try:
        contact_details = Contacts_Plus_Social_Media.objects.all()[0]
    except IndexError:
        contact_details = False

    services = Services.objects.all()
    projects = OurProjects.objects.all()

    form = ContactUsForm()
    
    
 

    return render(request, "main/sending_message_form_success.html", {"contact_details":contact_details,
                                                 "services":services,
                                                 "projects":projects,
                                                 })