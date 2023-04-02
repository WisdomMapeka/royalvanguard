from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Contacts_Plus_Social_Media(models.Model):
    opening_message = tinymce_models.HTMLField(null=True, blank=True, verbose_name="About Us Page Introduction Text", 
                                               help_text="Information added on this field will be displayed at the top of the contact page")
    address = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    open_hours = models.CharField(max_length=500, blank=True, null=True)
    facebook_link = models.CharField(max_length=1000, blank=True, null=True)
    twitter_link = models.CharField(max_length=1000, blank=True, null=True)
    instagram_link = models.CharField(max_length=1000, blank=True, null=True)
    youtube_link = models.CharField(max_length=1000, blank=True, null=True)
    linkedin_link = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'Contact Information plus social media details'
        verbose_name_plural = 'Contact Information plus social media details'

    def __str__(self):
        if self.address:
            return self.address
        else:
            return "Contacts"
            
class BackGroundImages(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, help_text="section where this backgound image is going to be displayed")
    img = models.ImageField(null=True, blank=True, upload_to="BackGroundImages/")

    def __str__(self):
        return self.name


class Slider(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    background_image = models.ImageField(upload_to="sliderIMages/", null=True, blank=True)

    class Meta:
        verbose_name = 'Slider Images and descriptions'
        verbose_name_plural = 'Slider Images and descriptions'

    def __str__(self):
        return self.title

class SummaryServices(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    summary = models.CharField(max_length=500, null=True, blank=True)
    incon = models.ImageField(upload_to="SummaryServices/", null=True, blank=True, verbose_name="Icon", help_text="This is a small image which represents a service added, you can download more from this webiste <a href='https://www.flaticon.com/' target='_blank' rel='noopener noreferrer'>Click To Download Icons</a>")

    class Meta:
        verbose_name = 'Brief Snippets Of services Offered [put only 3 items]'
        verbose_name_plural = 'Brief Snippets Of services Offered [put only 3 items]'

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    summary = models.CharField(max_length=500, null=True, blank=True)
    description = tinymce_models.HTMLField(null=True, blank=True, 
    help_text="Information added here, will be displayed on the about page, put as much as you can, eg history, values, mission and more")
    image = models.ImageField(upload_to="AboutUsImages/", null=True, blank=True)

    incon = models.ImageField(upload_to="AboutUsImages/", null=True, blank=True,
                              verbose_name="Icon", help_text="This is a small image which represents information added, you can download more from this webiste <a href='https://www.flaticon.com/' target='_blank' rel='noopener noreferrer'>Click To Download Icons</a>")
    incon_explanation = models.CharField(max_length=200, null=True, blank=True, default="4", verbose_name="Number Of Clients")
    incon_second_explanation = models.CharField(max_length=200, null=True, blank=True, default="Clients", verbose_name="Title", help_text="Title can be Clients or Any Other Word")

    incon2 = models.ImageField(upload_to="AboutUsImages/", null=True, blank=True,
                               verbose_name="Icon", help_text="This is a small image which represents information added, you can download more from this webiste <a href='https://www.flaticon.com/' target='_blank' rel='noopener noreferrer'>Click To Download Icons</a>")
    incon_explanation2 = models.CharField(max_length=200, null=True, blank=True, default="12", verbose_name="NUmber Of Projects")
    incon_second_explanation2 = models.CharField(max_length=200, null=True, blank=True, default="Projects", verbose_name="Title", help_text="Title can be Projects or Any Other Word")

    class Meta:
        verbose_name = 'About Us Information'
        verbose_name_plural = 'About Us Information'

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    summary = models.CharField(max_length=500, null=True, blank=True)
    description = tinymce_models.HTMLField(null=True, blank=True)
    incon = models.ImageField(upload_to="Services/", null=True, blank=True,
                              verbose_name="Icon", help_text="This is a small image which represents information added, you can download more from this webiste <a href='https://www.flaticon.com/' target='_blank' rel='noopener noreferrer'>Click To Download Icons</a>")

    class Meta:
        verbose_name = 'Services [max 6]'
        verbose_name_plural = 'Services [max 6]'

    def __str__(self):
        return self.title


class Sectors(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    summary = models.CharField(max_length=500, null=True, blank=True)
    incon = models.ImageField(upload_to="Services/", null=True, blank=True,
                              verbose_name="Icon", help_text="This is a small image which represents information added, you can download more from this webiste <a href='https://www.flaticon.com/' target='_blank' rel='noopener noreferrer'>Click To Download Icons</a>")

    class Meta:
        verbose_name = 'Sectors [max 6]'
        verbose_name_plural = 'Sectors [max 6]'

    def __str__(self):
        return self.title


class WhyChooseUsSummary(models.Model):
    summary = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to="WhyChooseUs/", null=True, blank=True)

    class Meta:
        verbose_name = 'Coming Soon Brief Information'
        verbose_name_plural = 'Coming Soon Brief Information'

    def __str__(self):
        return self.summary


class WhyChooseUs(models.Model):
    summary = models.ForeignKey(WhyChooseUsSummary, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = tinymce_models.HTMLField(null=True, blank=True)
    incon = models.ImageField(upload_to="WhyChooseUs/", null=True, blank=True,
                              verbose_name="Icon", help_text="This is a small image which represents information added, you can download more from this webiste <a href='https://www.flaticon.com/' target='_blank' rel='noopener noreferrer'>Click To Download Icons</a>")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Coming Soon'
        verbose_name_plural = 'Coming Soon'

OurProjects_choices = (
    ('first','completed'),
    ('second','on going')

)

class OurProjects(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="OurProjects/", null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True, choices=OurProjects_choices, default=True )

    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'


    def __str__(self):
        return self.title


class TeamMembers(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="TeamMembers/Profiles/", null=True, blank=True)
    facebook_link = models.TextField(null=True, blank=True)
    twitter_link = models.TextField(null=True, blank=True)
    instagram_link = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Team Members'
        verbose_name_plural = 'Team Members'


    def __str__(self):
        return self.name


class Testimonials(models.Model):
    client_name = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    profession = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="Testimonials/", null=True, blank=True)

    class Meta:
        verbose_name = 'Testimonials'
        verbose_name_plural = 'Testimonials'


    def __str__(self):
        return self.client_name


class ContactUs(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email  = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    message =  models.TextField(null=True, blank=True)
    sent = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Messages From Potential Clients'
        verbose_name_plural = 'Messages From Potential Clients'


    def __str__(self):
        return self.name










