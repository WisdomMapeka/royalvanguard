from django.shortcuts import render
from . models import Contacts_Plus_Social_Media, Slider, SummaryServices, AboutUs, Services, WhyChooseUsSummary, OurProjects, TeamMembers, Testimonials

# Create your views here.

def index(request):
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
                                               "testimonials":testimonials
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

    return render(request, "main/about.html", {"contact_details":contact_details,
                                               "about_us":about_us, })
