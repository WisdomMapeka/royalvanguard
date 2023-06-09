from django.contrib import admin
from .models import (Contacts_Plus_Social_Media, Slider, SummaryServices, 
                     AboutUs, Services, Feature, OurProjects,
                     TeamMembers, Testimonials, 
                     ContactUs, BackGroundImages, Sectors, OurBeliefs)

admin.site.register(BackGroundImages)
admin.site.register(OurBeliefs)

class  Contacts_Plus_Social_MediaAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone')

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'background_image')

class SummaryServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')

class SectorsAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')

class  FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')

class  OurProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class  TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

class  TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'image')

class  NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'email')

class  FeatureSummaryAdmin(admin.ModelAdmin):
    list_display = ('summary',)

class  ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')

class ShopHomePageLabelsAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')








admin.site.register(Contacts_Plus_Social_Media, Contacts_Plus_Social_MediaAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(SummaryServices, SummaryServicesAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Sectors, SectorsAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(OurProjects, OurProjectsAdmin)
admin.site.register(TeamMembers, TeamMembersAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(ContactUs, ContactUsAdmin)