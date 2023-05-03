from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Photo
from .forms import PhotoForm
import random


# Views for photo_site App


def index(request):
    """home page for photo_site"""
    photos = Photo.objects.all()
    x = random.randint(1, len(photos))
    photo_id = x
    photo = Photo.objects.get(id=photo_id)
    y = random.randint(1, len(photos))
    photo2_id = y
    photo2 = Photo.objects.get(id=photo2_id)
    context = {"photo": photo, "photo2": photo2}

    return render(request, "photo_site/index.html", context)


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
    current_user = request.user
    photo = Photo.objects.get(id=photo_id)
    context = {"photo": photo, "current_user": current_user}
    return render(request, "photo_site/photo.html", context)


@login_required
def my_photos(request):
    """display all photos uploaded by user"""
    my_photos = Photo.objects.filter(owner=request.user).order_by("-date_added")
    context = {"my_photos": my_photos}
    return render(request, "photo_site/my_photos.html", context)


@login_required
def edit_photo(request, photo_id):
    """User can edit their own photo"""
    photo = Photo.objects.get(id=photo_id)

    if request.method != "POST":
        form = PhotoForm(instance=photo)
    else:
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect("photo_site:my_photos")
    context = {"form": form, "photo": photo}
    return render(request, "photo_site/edit_photo.html", context)


# Add a view for editing photos if photo is one current user created
# possibly add a view my photos
