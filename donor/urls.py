from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="donor_register"),
    path("login", views.login_donor, name="donor_login"),
    path("", views.get_details, name="donor_details"),
    path("edit", views.update_details, name="donor_update")
]

# path("", views, name="donator_")
