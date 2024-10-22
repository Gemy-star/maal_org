from django.urls import path
from .views import HomeView, ContactView, AboutView , ProductView

urlpatterns = [
    path("", HomeView.as_view(), name="home-page"),
    path("contact", ContactView.as_view(), name="contact-page"),
    path("about", AboutView.as_view(), name="about-page"),
    path("products", ProductView.as_view(), name="product-page"),

]
