from django.urls import path

from . import views

urlpatterns = [
    # Owner/urls
    path("owner/register", views.register_owner, name="charity_owner_register"),
    path("owner/login", views.login_owner, name="charity_owner_login"),
    path("owner", views.get_owner_details, name="charity_owner_details"),
    path("owner/edit", views.update_charity, name="charity_owner_edit"),
    # Charity urls
    path("new", views.create_charity, name="charity_new"),
    path("", views.get_charities, name="charity_get_all"),
    path("<str:pk>", views.get_charity, name="charity_get_one"),
    path("<str:pk>/edit", views.update_charity, name="charity_edit"),
    path("<str:pk>/delete", views.delete_charity, name="charity_delete"),
]

# path("", views.,name="charity_"),
