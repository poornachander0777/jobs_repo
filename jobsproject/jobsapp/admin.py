from django.contrib import admin
from jobsapp.models import Hydjobs,Mumbaijobs,Husnabadjobs,Punejobs

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display=['CompanyName','JobName','Qualification','Experience','Salary','ContactNumber','Email','Address']
admin.site.register(Hydjobs,HydjobsAdmin)

class MumbaijobsAdmin(admin.ModelAdmin):
    list_display=['CompanyName','JobName','Qualification','Experience','Salary','ContactNumber','Email','Address']
admin.site.register(Mumbaijobs,MumbaijobsAdmin)

class HusnabadjobsAdmin(admin.ModelAdmin):
    list_display=['CompanyName','JobName','Qualification','Experience','Salary','ContactNumber','Email','Address']
admin.site.register(Husnabadjobs,HusnabadjobsAdmin)

class PunejobsAdmin(admin.ModelAdmin):
    list_display=['CompanyName','JobName','Qualification','Experience','Salary','ContactNumber','Email','Address']
admin.site.register(Punejobs,PunejobsAdmin)
