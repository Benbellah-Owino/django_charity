from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from .forms import OwnerRegisterForm, OwnerLoginForm, OwnerUpdateForm, CharityCreateForm, CharityUpdateForm
from .models import Owner, Charity


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
    form = OwnerRegisterForm()
    owners = Owner.objects.all()
    print("Owners: ",owners)

    if request.method == 'POST':
        form = OwnerRegisterForm(request.POST)
        print('Hey')
        if form.is_valid():
            print('Hey')
            new_owner = form.save()  # create Donator object but not save it yet
            print(form.cleaned_data)
            try:
                group = Group.objects.get(name='Charity_Owners')
            except Group.DoesNotExist:
                group = Group.objects.create(name='Charity_Owners')

            new_owner.groups.add(group)
            print(new_owner)


            return redirect('charity/login_owner)')
        else:
            print('Problems')
            print(form.errors)


    return render(request, 'owner/register/index.html', {'form': form})


def login_owner(request):
    """
           View function for handling requests to /charity/owner/login.

           Parameters:
           - request: The HTTP request object.

           Returns:
           -.
        """
    form = OwnerLoginForm()

    if request.method == "POST":
        form = OwnerLoginForm(request.POST)

        if form.is_valid():
            print("valid")
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # db_user = Owner.objects.get(email=email)
            # print(db_user.check_password(password))
            print(Owner.objects.all())

            owner = authenticate(request, email=email, password=password, model=Owner)
            print(owner)
            if owner is not None:
                login(request, owner)
                print("logged in")
            print(owner)

    return render(request, 'owner/login/index.html', {'form': form})


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
        form = OwnerUpdateForm(instance=owner)
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
    form = CharityCreateForm()

    if request.method == 'POST':
        form = CharityCreateForm(request.POST)

        if form.is_valid:
            charity = form.save(commit=False)
            charity.creator = request.user
            charity.save()

            #return confirmation

    return render(request, 'charity/new/index.html', {'form':form})


def get_charities(request):
    """
               View function for handling requests to /charity/.

               Parameters:
               - request: The HTTP request object.

               Returns:
               -.
            """
    #try:
    charities = Charity.objects.all()
    print(charities)

    return render(request, 'charity/list/index.html', {'charities':charities})
    # except :
    #     return HttpResponse('<center><h1 style="color:red">Error listing charity</h1></center>')



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
        return render(request, 'charity/index.html', {'charity': charity})
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
            return None  #
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
