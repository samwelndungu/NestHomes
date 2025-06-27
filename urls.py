from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from properties import views

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('properties.urls')),       # Routes /properties/ to your app
    path('contact/', views.contact_view, name='contact')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   