from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Donation


# Create your views here.
def make_donation(request):
    """
               View function for handling requests to /donation/.

               Parameters:
               - request: The HTTP request object.

               Returns:
               -.
            """
    # try:
    #     donation
    # except:
    return HttpResponse("<center><h1>Make donations </h1></center>")


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
