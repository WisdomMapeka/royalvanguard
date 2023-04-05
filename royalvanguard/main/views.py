from django.shortcuts import render
from . models import (Contacts_Plus_Social_Media, Slider, SummaryServices, 
                      AboutUs, Services, Feature, OurProjects, 
                      TeamMembers, Testimonials, ContactUs, BackGroundImages, Sectors)
from . forms import ContactUsForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def Trials(num, modelname):
    if modelname == "BackGroundImages":
        try:
            item = BackGroundImages.objects.all()[num]
        except IndexError:
            item = False

    elif modelname == "Contacts_Plus_Social_Media":
        try:
            item = Contacts_Plus_Social_Media.objects.all()[num]
        except IndexError:
            item = False

    elif modelname == "AboutUs":
        try:
            item = AboutUs.objects.all()[num]
        except IndexError:
            item = False

    elif modelname == "Feature":
        try:
            item = Feature.objects.all()[num]
        except IndexError:
            item = False

    return item
 
def index(request):
    
    sectors = Sectors.objects.all()
    slider = Slider.objects.all()
    service_summaries = SummaryServices.objects.all()
    services = Services.objects.all()
    projects = OurProjects.objects.all()
    teammembers = TeamMembers.objects.all()
    testimonials = Testimonials.objects.all()
    
    
    backgroundImage1 = Trials(0, "BackGroundImages")
    contact_details = Trials(0, "Contacts_Plus_Social_Media")
    about_us = Trials(0, "AboutUs")

  
    feature = Trials(0, "Feature")
    feature1 = Trials(1, "Feature")
    feature2 = Trials(2, "Feature")

    
    return render(request, "main/index.html", {"contact_details":contact_details,
                                               "slider":slider,
                                               "service_summaries":service_summaries,
                                               "about_us":about_us, 
                                               "services":services,
                                               "feature":feature,
                                               "feature1":feature1,
                                               "feature2":feature2,
                                               "projects":projects,
                                               "teammembers":teammembers,
                                               "testimonials":testimonials,
                                               "backgroundImage1":backgroundImage1,
                                               "sectors":sectors
                                               })


def about(request):
    backgroundImage1 = Trials(0, "BackGroundImages")
    backgroundImage2 = Trials(1, "BackGroundImages")
    backgroundImage3 = Trials(2, "BackGroundImages")
    backgroundImage4 = Trials(3, "BackGroundImages")
    backgroundImage5 = Trials(4, "BackGroundImages")
    contact_details = Trials(0, "Contacts_Plus_Social_Media")
    about_us = Trials(0, "AboutUs")
    teammembers = TeamMembers.objects.all()

    try:
        a = AboutUs.objects.all()[0]
        why_us = a.our_beliefs.filter(belief_type = "values")
        print(why_us.count())
    except IndexError:
        why_us = False
    

    return render(request, "main/about.html", {"contact_details":contact_details,
                                               "about_us":about_us,
                                               "teammembers":teammembers,
                                               "why_us":why_us,
                                               "backgroundImage1":backgroundImage1,
                                               "backgroundImage2":backgroundImage2,
                                               "backgroundImage3":backgroundImage3,
                                               "backgroundImage4":backgroundImage4,
                                               "backgroundImage5":backgroundImage5, })

def services(request):

    contact_details = Trials(0, "Contacts_Plus_Social_Media")
    services = Services.objects.all()
    return render(request, "main/service.html", {"contact_details":contact_details,
                                                 "services":services,})


def projects(request):
    contact_details = Trials(0, "Contacts_Plus_Social_Media")
    services = Services.objects.all()
    projects = OurProjects.objects.all()
    return render(request, "main/project.html", {"contact_details":contact_details,
                                                 "services":services,
                                                 "projects":projects,})

                    
def contacts(request):
    services = Services.objects.all()
    projects = OurProjects.objects.all()

    contact_details = Trials(0, "Contacts_Plus_Social_Media")

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
    services = Services.objects.all()
    projects = OurProjects.objects.all() 

    return render(request, "main/sending_message_form_success.html", {"contact_details":contact_details,
                                                 "services":services,
                                                 "projects":projects,
                                                 })