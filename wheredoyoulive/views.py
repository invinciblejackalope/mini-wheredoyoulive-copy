# Still need to replace ADDKEY with key in AddPOI. I also have some questions in AddPOI
#Also should we add ability to set home right when a user is made instead of making them update it

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import User
from .forms import CreateForm
import urllib.request
import urllib, json

# this is the basic structure for rendering and processing forms: most other
# pages are a variation on this (to avoid repetitiveness, comments explaining
# form code will be omitted for other pages)
def index(request):
    return render(request, 'wheredoyoulive/homepage.html', \
        {'make': reverse('wheredoyoulive:make'), \
        'index': reverse('wheredoyoulive:index')})

#Shows all users
def show_users(request):
    # list with the properties of every user
    uList = list(User.objects.all().values())
    return render(request, 'wheredoyoulive/listpage.html', \
        {'obj_list': uList, \
        'index': reverse('wheredoyoulive:index')})

#Makes new user
def make(request):
######### If you want to retrieve the data directly #########
    # if request.method == "POST": # or PATCH, etc.
    #     data = QueryDict(request.META["QUERY_STRING"]).dict()
    #     # do something with data, which will be a dictionary
    #     #   of all the keys and values passed in
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            #Makes sure username not already taken
            if (User.objects.filter(username=username)):
                # if it is, redirect to error page
                return render(request, 'wheredoyoulive/ErrorPage.html', \
                    {'error_name': 'Username already taken', \
                    'index': reverse('wheredoyoulive:index')})
            else:
                # create new user
                u = User(username=username, name=form.cleaned_data['name'])
                # gotta save manually
                u.save()
                return render(request, 'wheredoyoulive/homepage.html', \
                    {'page': reverse('wheredoyoulive:index')})

    else:
        form = CreateForm()
        return render(request, 'wheredoyoulive/FormPage.html', \
            {'form': form, \
            'page': reverse('wheredoyoulive:make')})
