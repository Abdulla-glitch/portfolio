from django.urls import path
from . import views
from django.http import HttpResponse

def empty_favicon(request):

    return HttpResponse(status=204)  # No Content

urlpatterns = [
    path('', views.home, name='home'),
    path('favicon.ico', empty_favicon),
    
]