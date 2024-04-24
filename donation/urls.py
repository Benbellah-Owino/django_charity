from django.urls import path

from . import views

urlpatterns = [
    path("", views.make_donation, name="donation_new"),
    path("charity/<str:pk>", views.get_donations, name="donation_get_all_charity"),
    path("<str:pk>", views.get_donation, name="donation_get_one"),
]

# path("", views.,name="donation_"),
