from django.shortcuts import render
from jobsapp.models import Hydjobs,Mumbaijobs,Husnabadjobs,Punejobs
# Create your views here.
def Home_view(request):
    return render(request,"jobsapp/home.html")
def Hydjobs_view(request):
    Hydjobs_list=Hydjobs.objects.all()
    my_dict={"Hydjobs_list":Hydjobs_list}
    return render(request,"jobsapp/hydjobs.html",my_dict)
def Mumbaijobs_view(request):
    Mumbaijobs_list=Mumbaijobs.objects.all()
    my_dict={"Mumbaijobs_list":Mumbaijobs_list}
    return render(request,"jobsapp/mumbaijobs.html",my_dict)
def Husnabadjobs_view(request):
    Husnabadjobs_list=Husnabadjobs.objects.all()
    my_dict={"Husnabadjobs_list":Husnabadjobs_list}
    return render(request,"jobsapp/husnabadjobs.html",my_dict)
def Punejobs_view(request):
    Punejobs_list=Punejobs.objects.all()
    my_dict={"Punejobs_list":Punejobs_list}
    return render(request,"jobsapp/punejobs.html",my_dict)
