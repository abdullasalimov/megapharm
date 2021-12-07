from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shop/", views.shop, name="shop"),
    path("shop/<slug:slug>", views.detail, name="detail"),
    path("shop/search/", views.search, name="search"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("thankyou/", views.thankyou, name="thankyou"),
]
