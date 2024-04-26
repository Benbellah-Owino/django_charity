from django.urls import path

from . import views

app_name='donor'
urlpatterns = [
    path("register", views.register, name="donor_register"),
    path("login", views.login_donor, name="donor_login"),
    path("", views.get_details, name="donor_details"),
    path("edit", views.update_details, name="donor_update"),
    path("logout", views.logout_donor, name="donor_logout")
]

# path("", views, name="donator_")
