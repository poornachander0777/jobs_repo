from django.urls import path
from jobsapp import views

urlpatterns = [
path("" , views.Home_view),
path("hydjobs/" , views.Hydjobs_view),
path("husnabadjobs/" , views.Husnabadjobs_view),
path("mumbaijobs/" , views.Mumbaijobs_view),
path("punejobs/" , views.Punejobs_view),
]
