from django.db import models

# Create your models here.
class Contacts_Plus_Social_Media(models.Model):
    address = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.ImageField(upload_to="socialMedia/", blank=True, null=True)
    twitter = models.ImageField(upload_to="socialMedia/", blank=True, null=True)
    instagram = models.ImageField(upload_to="socialMedia/", blank=True, null=True)
    youtube = models.ImageField(upload_to="socialMedia/", blank=True, null=True)
    linkedin = models.ImageField(upload_to="socialMedia/", blank=True, null=True)

    def __str__(self):
        return self.address


class Slider(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    background_image = models.ImageField(upload_to="sliderIMages/", null=True, blank=True)

    def __str__(self):
        return self.title

