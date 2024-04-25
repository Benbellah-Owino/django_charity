from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Donation
from .forms import DonationForm
from uuid6 import uuid6

# Create your views here.
def make_donation(request):
    """
               View function for handling requests to /donation/.

               Parameters:
               - request: The HTTP request object.

               Returns:
               -.
            """

    reference = uuid6()
    print(reference)
    if request.method == 'POST':
        donation_amount = DonationForm(request.POST)
        if donation_amount.is_valid():
            print(donation_amount.cleaned_data)
            donation = donation_amount.save(commit=False)
            donation.reference_msg = reference
            donation.donor = request.user
            charity = donation.charity
            print(charity.id)
            charity.total_donations+= donation.amount
            print(charity.total_donations)
            charity.save()
            donation.save()
            #TODO: Finish this

            #donation.charity

            return HttpResponse('<h1><center>Payment made</center></h1>')
    return HttpResponse('<h1><center>Payment </center></h1>')





@login_required
def get_donations(request, pk):
    """
               View function for handling requests to /donation/charity/<str:pk>.

               Parameters:
               - request: The HTTP request object.

               Returns:
               -.
            """
    try:
        donations = Donation.objects.filter(charity=pk)
        return donations
    except:
        return None
    return HttpResponse("<center><h1>Get donations </h1></center>")


@login_required
def get_donation(request, pk):
    """
               View function for handling requests to /donation/<str:pk>.

               Parameters:
               - request: The HTTP request object.

               Returns:
               -.
            """
    try:
        charity = Donation.object.get(id=pk)
    except:
        return None
    return HttpResponse("<center><h1>Make donations </h1></center>")


def return_donations(request):
    """
               View function for handling requests to /donation/charity/<str:pk>/return/.

               Parameters:
               - request: The HTTP request object.

               Returns:
               -.
            """
    return HttpResponse("<center><h1>Get donations </h1></center>")
