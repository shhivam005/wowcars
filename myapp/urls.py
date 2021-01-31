from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.index,name="default"),
    path("about/",views.about,name="about"),
    path("cars/",views.cars,name="cars"),
    path("cardetails/<int:myid>",views.carDetails,name="car-details"),
    path("contact/",views.contact,name="contact"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)