from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import render, redirect

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
                new_donor = form.save(commit=False)  # create Donator object but not save it yet

                try:
                    group = Group.objects.get(name='Donors')
                except Group.DoesNotExist:
                    group = Group.objects.create(name='Donor')

                new_donor.groups.add(group)
                print(new_donor)
                new_donor.save()

                return redirect('donor/login_donor')


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

            db_user = Donor.objects.get(email=email)
            print(db_user.check_password(password))
            print("Email: ", db_user.email)
            print("Password: ", db_user.password)
            print("Is active: ", db_user.is_active)
            user = authenticate(email=email, password=password, model=Donor)
            print(user)
            if user is not None:
                login(request, user)
                print("logged in")

    return render(request, 'login/index.html', {'form': form})


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
        donations = Donor.donations.all()
        #return the owner object
    except Donor.DoesNotExist:
        return HttpResponse('<center><h1 style="color:red">Donor does not exists</h1></center>')
    return HttpResponse("<center><h1>Details</h1></center>")


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
