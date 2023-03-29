from django.contrib import admin
from .models import (Contacts_Plus_Social_Media, Slider, SummaryServices, 
                     AboutUs, Services, WhyChooseUs, OurProjects,
                     TeamMembers, Testimonials, NewsLetter , WhyChooseUsSummary)

class  Contacts_Plus_Social_MediaAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone')

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'background_image')

class SummaryServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'background_image')

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')

class  WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')

class  OurProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

# class  FreeQuoteAdmin(admin.ModelAdmin):
#     list_display = ('title', 'summary')

class  TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

class  TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'image')

class  NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'email')

class  WhyChooseUsSummaryAdmin(admin.ModelAdmin):
    list_display = ('summary',)








admin.site.register(Contacts_Plus_Social_Media, Contacts_Plus_Social_MediaAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(SummaryServices, SummaryServicesAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(WhyChooseUs, WhyChooseUsAdmin)
admin.site.register(WhyChooseUsSummary, WhyChooseUsSummaryAdmin)
admin.site.register(OurProjects, OurProjectsAdmin)
# admin.site.register(FreeQuote, FreeQuoteAdmin)
admin.site.register(TeamMembers, TeamMembersAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)