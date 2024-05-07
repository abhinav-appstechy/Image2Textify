from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('about-us', views.about_us, name="about_us"),
    path('contact-us', views.contact_us, name="contact_us"),
    path('logout', views.logout_view, name="logout"),
    path('extract', views.extract, name="extract"),
]