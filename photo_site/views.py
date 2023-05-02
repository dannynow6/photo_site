from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Photo
from .forms import PhotoForm


# Views for photo_site App


def index(request):
    """home page for photo_site"""
    return render(request, "photo_site/index.html")


# Require users to have an account before uploading a photo
@login_required
def add_photo(request):
    """a page for adding a new photo"""
    if request.method != "POST":
        form = PhotoForm()
    else:
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.owner = request.user
            new_photo.save()
            return redirect("photo_site:index")

    context = {"form": form}
    return render(request, "photo_site/add_photo.html", context)


def photos(request):
    """a page to view photos uploaded by users"""
    photos = Photo.objects.order_by("-date_added")
    context = {"photos": photos}
    return render(request, "photo_site/photos.html", context)


def photo(request, photo_id):
    """Show the details of a specific photo"""
    photo = Photo.objects.get(id=photo_id)
    context = {"photo": photo}
    return render(request, "photo_site/photo.html", context)
