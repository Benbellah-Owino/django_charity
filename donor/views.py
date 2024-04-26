from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import DonorRegisterForm, DonorLoginForm, DonorUpdateForm
from .models import Donor


# Create your views here.
def register(request):
    """
                   View function for handling requests to /donator/register.

                   Parameters:
                   - request: The HTTP request object.

                   Returns:
                   -.
                """
    form = DonorRegisterForm()
    try:

        if request.method == 'POST':
            form = DonorRegisterForm(request.POST)

            if form.is_valid():
                cd = form.clean()
                print(cd)
                new_donor = form.save()  # create Donator object but not save it yet

                try:
                    group = Group.objects.get(name='Donors')
                except Group.DoesNotExist:
                    group = Group.objects.create(name='Donors')
                print(group)
                new_donor.groups.add(group)
                print(new_donor)
                new_donor.save()

                donor_login = reverse('donor:donor_login')
                return redirect(donor_login)


            else:
                print(form.errors)
                raise ValidationError('Form Has Error')

    except ValidationError:
        print(form.errors)
        return HttpResponse('<center><h1 style="color:red">Register Error 1</h1></center>')
    return render(request, "register/index.html", {'form': form})


def login_donor(request):
    """
                       View function for handling requests to /donator/login.

                       Parameters:
                       - request: The HTTP request object.

                       Returns:
                       -.
                    """
    #return HttpResponse('<center><h1 style="color:red">Login Error</h1></center>')
    form = DonorLoginForm()
    if request.method == "POST":

        form = DonorLoginForm(request.POST)

        if form.is_valid():
            print("valid")
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # db_user = Donor.objects.get(email=email)
            # print(db_user.check_password(password))
            # print("Email: ", db_user.email)
            # print("Password: ", db_user.password)

            user = authenticate(email=email, password=password, model=Donor)
            print(user)
            if user is not None:
                login(request, user)
                print("logged in")
                charity_url = reverse('charity:charity_get_all')
                return redirect(charity_url)

    return render(request, 'login/index.html', {'form': form})

@login_required
def get_details(request):
    """
                       View function for handling requests to /donator/.

                       Parameters:
                       - request: The HTTP request object.

                       Returns:
                       -.
                    """
    try:
        donor_object = request.user
        donor = Donor.objects.get(email=donor_object.email)
        donations = donor.donations.all()

        for donation in donations:
            print(donation.charity)
        context = {
            'donor': donor,
            'donations':donations
        }
        return render(request, 'details/index.html', context)
    except Donor.DoesNotExist:
        return HttpResponse('<center><h1 style="color:red">Donor does not exists</h1></center>')
    return HttpResponse("<center><h1>Details</h1></center>")

@login_required
def update_details(request):
    """
                       View function for handling requests to /donator/edit.

                       Parameters:
                       - request: The HTTP request object.

                       Returns:
                       -.
                    """
    try:
        donor = request.user
        form = DonorUpdateForm(instance=donor)
        if request.method == "POST":

            if form.is_valid():
                print(form.cleaned_data)
                form.save()
                #return
    except:
        return HttpResponse('<center><h1 style="color:red">Error updating donor</h1></center>')
    return HttpResponse("<center><h1>Upd ate details</h1></center>")

@login_required
def logout_donor(request):
        logout(request)
        login_url = reverse('donor:donor_login')
        return redirect(login_url)  # Redirect to the home page after logout