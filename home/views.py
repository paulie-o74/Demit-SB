from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def collabs(request):
    """ A view to return the collabs page """

    return render(request, 'home/collabs.html')


def murals(request):
    """ A view to return the murals page """

    return render(request, 'home/murals.html')


def paintings(request):
    """ A view to return the paintings page """

    return render(request, 'home/paintings.html')


def contact(request):
    """ A view to return the contact page """

    return render(request, 'home/contact.html')