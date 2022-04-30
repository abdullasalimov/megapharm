from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shop/", views.shop, name="shop"),
    path("shop/<slug:slug>/", views.detail, name="detail"),
    path("shop/search/", views.search, name="search"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login_page, name="login"),
    path("signup/", views.signup_page, name="signup"),
    path("logout/", views.logout_page, name="logout"),
    path("shop/<slug:slug>/thankyou/<slug:slug1>/", views.thankyou, name="thankyou"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
