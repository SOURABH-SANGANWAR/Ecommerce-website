from django.shortcuts import render
from django.contrib.auth import login
from CustomUser.models import CustomUser

# Create your views here.
# def Myfun(requests,*args,**kwargs):
#     if(requests.POST):
#         user = CustomUser.objects.get(id = 1)
#         login(requests,user)
#     return render(requests,'index.html',{'ranges' : range(5)})
