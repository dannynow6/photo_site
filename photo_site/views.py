from django.shortcuts import render


# Views for photo_site App


def index(request):
    """home page for photo_site"""
    return render(request, "photo_site/index.html")
