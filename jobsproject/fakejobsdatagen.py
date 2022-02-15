import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsproject.settings')

import django
django.setup()

from jobsapp.models import Hydjobs,Mumbaijobs,Husnabadjobs,Punejobs
from faker import Faker
from random import *

def phonenumbergen():
    d1=randint(6,9)
    num=str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

fake=Faker()
def fakedatagen(n):
    for i in range(n):
        fCompanyName=fake.name()
        fJobName=fake.random_element(elements=('Jr.Software Developer','Sr.Software Developer','Team Leader','HR','CEO'))
        fQualification=fake.random_element(elements=('10th','InterMediate','Btech','Mtech','PG','Any Degree','PHD'))
        fExperience=fake.random_element(elements=('1Year','2Years','3Years','4Years','5Years'))
        fSalary=fake.random_int(min=50000,max=100000)
        fContactNumber=phonenumbergen()
        fEmail=fake.email()
        fAddress=fake.address()
        fakedata_record=Husnabadjobs.objects.get_or_create(
              CompanyName=fCompanyName,
              JobName=fJobName,
              Qualification=fQualification,
              Experience=fExperience,
              Salary=fSalary,
              ContactNumber=fContactNumber,
              Email=fEmail,
              Address=fAddress)
        fakedata_record=Hydjobs.objects.get_or_create(
              CompanyName=fCompanyName,
              JobName=fJobName,
              Qualification=fQualification,
              Experience=fExperience,
              Salary=fSalary,
              ContactNumber=fContactNumber,
              Email=fEmail,
              Address=fAddress)
        fakedata_record=Mumbaijobs.objects.get_or_create(
              CompanyName=fCompanyName,
              JobName=fJobName,
              Qualification=fQualification,
              Experience=fExperience,
              Salary=fSalary,
              ContactNumber=fContactNumber,
              Email=fEmail,
              Address=fAddress)
        fakedata_record=Punejobs.objects.get_or_create(
              CompanyName=fCompanyName,
              JobName=fJobName,
              Qualification=fQualification,
              Experience=fExperience,
              Salary=fSalary,
              ContactNumber=fContactNumber,
              Email=fEmail,
              Address=fAddress)

n=int(input("enter any number to generate fake data:"))
fakedatagen(n)
print(f"{n} times fake data generated successfully...!!!")
