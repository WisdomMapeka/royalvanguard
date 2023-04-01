from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),

]
urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Royal Vanguard'                    # default: "Django Administration"
admin.site.index_title = 'Royal Vanguard'               # default: "Site administration"
admin.site.site_title = 'Royal Vanguard'  # default: "Django site admin"


