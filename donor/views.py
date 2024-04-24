from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

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
    try:
        if request.method == 'POST':
            form = DonorRegisterForm(request.POST)
            if form.isvalid():
                new_donator = form.save()  # create Donator object but not save it yet
                print(new_donator)


            #redirect to login
    except:
        return 'Error'
    return HttpResponse("<center><h1>Register page</h1></center>")


def login(request):
    """
                       View function for handling requests to /donator/login.

                       Parameters:
                       - request: The HTTP request object.

                       Returns:
                       -.
                    """
    try:
        if request.method == "POST":
            form = DonorLoginForm(request.POST)

            if form.is_valid():
                print("valid")
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                print(email)
                print(password)
                user = authenticate(request, email=email, password=password, model=Donor)
                print(user)
    except:
        return HttpResponse('<center><h1 style="color:red">Login Error</h1></center>')
    return HttpResponse("<center><h1>Login Page</h1></center>")


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
        form = DonorUpdateForm(instance = donor)
        if request.method == "POST":

            if form.is_valid():
                print(form.cleaned_data)
                form.save()
                #return
    except:
        return HttpResponse('<center><h1 style="color:red">Error updating donor</h1></center>')
    return HttpResponse("<center><h1>Upd ate details</h1></center>")
