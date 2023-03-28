from django.shortcuts import render
from . models import Contacts_Plus_Social_Media, Slider, SummaryServices, AboutUs, Services, WhyChooseUsSummary, OurProjects, TeamMembers

# Create your views here.

def index(request):
    contact_details = Contacts_Plus_Social_Media.objects.all()[0]
    slider = Slider.objects.all()
    service_summaries = SummaryServices.objects.all()
    services = Services.objects.all()
    projects = OurProjects.objects.all()
    teammembers = TeamMembers.objects.all()
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
                                               "teammembers":teammembers})
