from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse
import csv

def insert_bank(self):
    with open('C:\\Users\\B RANGA SHWETA\\OneDrive\\Desktop\\django projects\\swetha\\Scripts\\project42\\app\\bank.csv','r') as FO:
     IOD=csv.reader(FO)
     for i in IOD:
        bn=i[0].strip()
        BO=Bank(bank_name=bn)
        BO.save()

    return HttpResponse('Bank data is inserted sucessfully')

def insert_branch(self):
   with open ('C:\\Users\\B RANGA SHWETA\\OneDrive\\Desktop\\django projects\\swetha\\Scripts\\project42\\app\\branch1.csv','r')as FO:
      IOD=csv.reader(FO)
      for i in IOD:
         next(IOD)
         bn=i[0]
         BO=Bank.objects.filter(bank_name=bn)
         if BO:
            ifs=i[1]
            br=i[2]
            ad=i[3]
            co=i[4]
            ci=i[5]
            dis=i[6]
            st=i[7] 

            BRO=Branch(bank_name=BO[0],IFSC=ifs,branch=br,address=ad,contact=co,city=ci,District=dis,state=st)
            BRO.save()
   return HttpResponse ('Branch data is inserted sucessfully done')

