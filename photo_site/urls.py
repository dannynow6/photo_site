from django.conf import settings 
from django.conf.urls.static import static 
from django.urls import path 
from . import views 

app_name = "photo_site" 
urlpatterns = [
    # Home page 
    path("", views.index, name="index"), 
    # Add photo page 
    path("add_photo/", views.add_photo, name="add_photo"), 
    # View photos uploaded by users 
    path("photos/", views.photos, name="photos"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 