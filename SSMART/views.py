from atexit import register
from django.shortcuts import render,get_object_or_404,redirect

from django.contrib.auth.decorators import login_required
# from Cus.models import Account
from products.models import Product,SuperCategory,Category
from products.models import Offers
from products.models import BestSellers
from django.views import View
# from .forms import MakeForm
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from CustomUser.models import CustomUser
# Create your views here.
def home_view(requests):
    x = Product.objects.all()
    y = Offers.objects.get(id = 1).Product_list.all()
    leny  =(len(y)+1)*230
    z = BestSellers.objects.get(id = 1).Product_list.all()
    lenz  =(len(z)+1)*230
    # z= x.Sellers.all()
    context = {
        'obj' : x,
        'off' : y,
        'numOff':leny,
        'numTop':lenz,
        'best': z, 
        'login': False,
        'requests':requests
        }
    if(requests.user.is_authenticated):
        context['login'] = True
    return render(requests,'index.html',context)

def Cat_view(requests):
    x = SuperCategory.objects.all()
    return render(requests,'categories.html',{'categories':x,'requests':requests})

def login_page(requests):
    if(requests.user.is_authenticated):
        return redirect('homeView')
    message = None
    if requests.method == 'POST':
        emailGot = requests.POST.get('email')
        try:
            x = CustomUser.objects.get(email = emailGot)
            if x is not None:
                obj = authenticate(email=requests.POST.get('email'), password=requests.POST.get('password'))
                if obj is not None:
                    login(requests,obj)
                    return redirect(str(requests.GET.get('next')))
                else:
                    message = 'ERROR! : wrong EmailId'
            else:
                message = 'ERROR! :User nor found.'
        except:
            message = 'ERROR! :User nor found.'
    return render(requests,'login.html',{'message':message})


def logout_page(requests):
    logout(requests)
    return redirect('homeView')
def offers(requests):
    y = Offers.objects.get(id = 1).Product_list.all()
    if requests.method =='POST':
        if 'category' in requests.POST:
            y = y.filter(category__id = requests.POST.get('cats'))
            # return  redirect('Products:detail_view_filter',id = requests.POST.get('cats'))
        elif 'search' in requests.POST:
            return  redirect('Products:search',search=requests.POST.get('search'))
    return render(requests,'Product_list.html',{'prods':y, 'desc':'Offers:','cats': Category.objects.all(),'requests':requests})

@login_required
def profile(requests):
    user = requests.user
    return render(requests,'profile.html',{'user':user, 'requests':requests})

def register(requests):
    if requests.method =='POST':
        # x = CustomUser.objects.create_user(username = requests.POST.get('username'),email = requests.POST.get('email'),first_name = requests.POST.get('f_name'), last_name = requests.POST.get('l_name'), phone_no = requests.POST.get('number'), address = requests.POST.get('address'))
        x = CustomUser.objects.create_user(email = requests.POST.get('email'))
        x.set_password(requests.POST.get('password'))
        x.save()
        login(requests,x)
        x.MyOrders.create(netPrice = 0,customer = requests.user)
        x.username = requests.POST.get('username')
        x.first_name = requests.POST.get('f_name')
        x.last_name = requests.POST.get('l_name')
        x.address = requests.POST.get('address')
        x.phone_no = requests.POST.get('number')
        x.save()
        return redirect('/')
    return render(requests,'register.html',{})
