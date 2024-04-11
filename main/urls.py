from django.urls import path
from .views import HomeView, ContactView, AboutView

urlpatterns = [
    path("", HomeView.as_view(), name="home-page"),
    path("contact", ContactView.as_view(), name="contact-page"),
    path("about", AboutView.as_view(), name="about-page"),
]
