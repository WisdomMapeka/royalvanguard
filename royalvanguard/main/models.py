from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Contacts_Plus_Social_Media(models.Model):
    opening_message = tinymce_models.HTMLField(null=True, blank=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    open_hours = models.CharField(max_length=500, blank=True, null=True)
    facebook_link = models.CharField(max_length=1000, blank=True, null=True)
    twitter_link = models.CharField(max_length=1000, blank=True, null=True)
    instagram_link = models.CharField(max_length=1000, blank=True, null=True)
    youtube_link = models.CharField(max_length=1000, blank=True, null=True)
    linkedin_link = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        if self.address:
            return self.address
        else:
            return "Contacts"


class Slider(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    background_image = models.ImageField(upload_to="sliderIMages/", null=True, blank=True)

    def __str__(self):
        return self.title

class SummaryServices(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    summary = models.CharField(max_length=500, null=True, blank=True)
    incon = models.ImageField(upload_to="SummaryServices/", null=True, blank=True)
    background_image = models.ImageField(upload_to="SummaryServices/", null=True, blank=True)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    summary = models.CharField(max_length=500, null=True, blank=True)
    description = tinymce_models.HTMLField(null=True, blank=True)
    image = models.ImageField(upload_to="AboutUsImages/", null=True, blank=True)

    incon = models.ImageField(upload_to="AboutUsImages/", null=True, blank=True)
    incon_explanation = models.CharField(max_length=200, null=True, blank=True)
    incon_second_explanation = models.CharField(max_length=200, null=True, blank=True)

    incon2 = models.ImageField(upload_to="AboutUsImages/", null=True, blank=True)
    incon_explanation2 = models.CharField(max_length=200, null=True, blank=True)
    incon_second_explanation2 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    summary = models.CharField(max_length=500, null=True, blank=True)
    description = tinymce_models.HTMLField(null=True, blank=True)
    incon = models.ImageField(upload_to="Services/", null=True, blank=True)

    def __str__(self):
        return self.title


class WhyChooseUsSummary(models.Model):
    summary = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to="WhyChooseUs/", null=True, blank=True)

    def __str__(self):
        return self.summary


class WhyChooseUs(models.Model):
    summary = models.ForeignKey(WhyChooseUsSummary, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    incon = models.ImageField(upload_to="WhyChooseUs/", null=True, blank=True)

    def __str__(self) -> str:
        return self.title

OurProjects_choices = (
    ('first','completed'),
    ('second','on going')

)

class OurProjects(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="OurProjects/", null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True, choices=OurProjects_choices, default=True )

    def __str__(self):
        return self.title


class TeamMembers(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="TeamMembers/Profiles/", null=True, blank=True)
    facebook_link = models.TextField(null=True, blank=True)
    twitter_link = models.TextField(null=True, blank=True)
    instagram_link = models.TextField(null=True, blank=True)
   

    def __str__(self):
        return self.name


class Testimonials(models.Model):
    client_name = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    profession = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="Testimonials/", null=True, blank=True)

    def __str__(self):
        return self.client_name

class NewsLetter(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    summary = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email  = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    message =  models.TextField(null=True, blank=True)
    sent = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name



class ShopHomePageLabels(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    summary = models.CharField(max_length=500, null=True, blank=True)
    description = tinymce_models.HTMLField(null=True, blank=True)
    image = models.ImageField(upload_to="AboutUsImages/", null=True, blank=True)

    incon = models.ImageField(upload_to="AboutUsImages/", null=True, blank=True)
    incon_explanation = models.CharField(max_length=200, null=True, blank=True)
    incon_second_explanation = models.CharField(max_length=200, null=True, blank=True)

    incon2 = models.ImageField(upload_to="AboutUsImages/", null=True, blank=True)
    incon_explanation2 = models.CharField(max_length=200, null=True, blank=True)
    incon_second_explanation2 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title









