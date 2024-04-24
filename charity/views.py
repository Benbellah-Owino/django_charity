from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .forms import OwnerRegisterForm, OwnerLoginForm, OwnerUpdateForm, CharityCreateForm, CharityUpdateForm
from .models import Owner,Charity


# Create your views here.
# Charity owner
def register_owner(request):
    """
       View function for handling requests to /owner/register.

       Parameters:
       - request: The HTTP request object.

       Returns:
       -.
    """
    try:
        if request.method == 'POST':
            form = OwnerRegisterForm(request.POST)
            if form.isvalid():
                new_owner = form.save()  # create Donator object but not save it yet
                print(new_owner)

            # redirect to login
    except:
        return 'Error'
    return HttpResponse("<center><h1>Register owner page</h1></center>")


def login_owner(request):
    """
           View function for handling requests to /charity/owner/login.

           Parameters:
           - request: The HTTP request object.

           Returns:
           -.
        """
    
    try:
        if request.method == "POST":
            form = OwnerLoginForm(request.POST)

            if form.is_valid():
                print("valid")
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                print(email)
                print(password)
                owner = authenticate(request, email=email, password=password, model=Owner)
                print(owner)
    except:
        return HttpResponse('<center><h1 style="color:red">Login Error</h1></center>')
    return HttpResponse("<center><h1>Login owner Page</h1></center>")

@login_required
def get_owner_details(request):
    """
           View function for handling requests to /charity/owner/.

           Parameters:
           - request: The HTTP request object.

           Returns:
           -.
        """
    try:
        owner_object = request.user
        owner = Owner.objects.get(email=owner_object.email)
        donations = Owner.donations.all()
        context = {
            owner: owner,
            donations: donations
        }
        #return the owner object
    except Owner.DoesNotExist:
        return HttpResponse('<center><h1 style="color:red">Owner does not exists</h1></center>')
    return HttpResponse("<center><h1>Details owner</h1></center>")

@login_required
def update_owner_details(request):
    """
           View function for handling requests to /charity/owner/edit.

           Parameters:
           - request: The HTTP request object.

           Returns:
           -.
        """
    try:
        owner = request.user
        form = OwnerUpdateForm(instance = owner)
        if request.method == "POST":

            if form.is_valid():
                print(form.cleaned_data)
                form.save()
                #return
    except:
        return HttpResponse('<center><h1 style="color:red">Error updating Owner</h1></center>')
    return HttpResponse("<center><h1>Update owner details </h1></center>")


@login_required
def create_charity(request):
    """
           View function for handling requests to /charity/new.

           Parameters:
           - request: The HTTP request object.

           Returns:
           -.
        """
    try:
        if request.method == 'POST':
            form = CharityCreateForm(request.POST)

            if form.is_valid:
                charity = form.save(commit=False)
                charity.creator = request.user
                charity.save()

            #return confirmation

    except:
        return HttpResponse('<center><h1 style="color:red">Error Creating charity</h1></center>')

    return HttpResponse("<center><h1> charity </h1></center>")


def get_charities(request):
    """
               View function for handling requests to /charity/.

               Parameters:
               - request: The HTTP request object.

               Returns:
               -.
            """
    try:
        charities = Charity.objects.all()
        print(charities)

        #return render
    except:
        return HttpResponse('<center><h1 style="color:red">Error Creating charity</h1></center>')
    return HttpResponse("<center><h1>Get charities </h1></center>")



def get_charity(request, pk):
    """
               View function for handling requests to /charity/<str:pk>.

               Parameters:
               - request: The HTTP request object.

               Returns:
               -.
            """
    try:
        charity = Charity.objects.get(id=pk)
        # Donations
    except:
        return HttpResponse('<center><h1 style="color:red">Error fetching charity</h1></center>')

    return HttpResponse("<center><h1>Get charity </h1></center>")


@login_required
def update_charity(request, pk):
    """
               View function for handling requests to /charity/<str:pk>/edit.

               Parameters:
               - request: The HTTP request object.

               Returns:
               -.
            """
    try:
        charity = Charity.objects.get(id=pk)

        if Charity.creator != request.user.id:
            print(request)
            return None #
        else:
            form = CharityUpdateForm(instance=charity)

            if request.method == 'POST':
                form = CharityUpdateForm(request.POST, instance=charity)

                if form.is_valid():
                    charity = form.save()

                    #return redirect to charity page

            return HttpResponse("<center><h1>Edit charity </h1></center>")
    except:
        return HttpResponse('<center><h1 style="color:red">Error fetching charity</h1></center>')


@login_required
def delete_charity(request, pk):
    """
               View function for handling requests to /charity/<str:pk>/delete.

               Parameters:
               - request: The HTTP request object.

               Returns:
               -.
            """
    try:
        charity = Charity.objects.get(id=pk)

        if charity.creator != request.user.id:
            return None
        else:
            charity.delete()
            #return response/json
    except:
        return HttpResponse('<center><h1 style="color:red">Error deleting charity</h1></center>')

    return HttpResponse("<center><h1>Delete charity </h1></center>")
