from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


# Use the login_required() decorator to ensure only 
# those logged in can access the view.
@login_required
def user_logout(request):
    logout(request)