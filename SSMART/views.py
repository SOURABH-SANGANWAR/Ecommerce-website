from atexit import register
from django.shortcuts import render,get_object_or_404,redirect

from django.contrib.auth.decorators import login_required
from products.models import Product,SuperCategory,Category
from products.models import Offers
from products.models import BestSellers
from django.views import View
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from CustomUser.models import CustomUser
# Create your views here.


def home_view(requests):
    x = Product.objects.all()
    try:
        y = Offers.objects.get(id = 1).Product_list.all()
        leny  =(len(y)+1)*230
    except:
        leny = 230
        y = None
    try:
        z = BestSellers.objects.get(id = 1).Product_list.all()
        lenz  =(len(z)+1)*230
    except:
        lenz = 230
        z = None
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
        print(1)
        emailGot = requests.POST.get('email')
        print(2)
        try:
            print(3)
            x = CustomUser.objects.get(email = emailGot)
            print(4)
            if x is not None:
                print(5)
                obj = authenticate(email=requests.POST.get('email'), password=requests.POST.get('password'))
                print(6)
                if obj is not None:
                    print(7)
                    login(requests,obj)
                    print(8)
                    try:
                        return redirect(str(requests.GET.get('next')))
                    except:
                        return redirect('homeView')
                else:
                    message = 'ERROR! : wrong Password'
            else:
                message = 'ERROR! :User nor found.'
        except:
            message = 'ERROR! :User nor found.'
    return render(requests,'login.html',{'message':message})


def logout_page(requests):
    logout(requests)
    return redirect('homeView')
def offers(requests):
    try:
        y = Offers.objects.get(id = 1).Product_list.all()
        leny  =(len(y)+1)*230
    except:
        leny = 230
        y = None
    if requests.method =='POST':
        if 'category' in requests.POST:
            y = y.filter(category__id = requests.POST.get('cats'))
            # return  redirect('Products:detail_view_filter',id = requests.POST.get('cats'))
        elif 'search' in requests.POST:
            return  redirect('Products:search',search=requests.POST.get('search'))
    return render(requests,'Product_list.html',{'prods':y, 'desc':'Offers:','cats': Category.objects.all(),'requests':requests})



def BestSellers(requests):
    try:
        y = BestSellers.objects.get(id = 1).Product_list.all()
        lenz  =(len(y)+1)*230
    except:
        lenz = 230
        y = None
    if requests.method =='POST':
        if 'category' in requests.POST:
            y = y.filter(category__id = requests.POST.get('cats'))
            # return  redirect('Products:detail_view_filter',id = requests.POST.get('cats'))
        elif 'search' in requests.POST:
            return  redirect('Products:search',search=requests.POST.get('search'))
    return render(requests,'Product_list.html',{'prods':y, 'desc':'BestSellers:','cats': Category.objects.all(),'requests':requests})




@login_required
def profile(requests):
    user = requests.user
    return render(requests,'profile.html',{'user':user, 'requests':requests})

@login_required
def updateDetail(requests):
    user = requests.user
    if requests.method =='POST':
        x = requests.user
        x.first_name = requests.POST.get('first_name')
        x.last_name = requests.POST.get('last_name')
        x.address = requests.POST.get('address')
        x.phone_no = requests.POST.get('phone_no')
        x.city = requests.POST.get('city')
        x.country = requests.POST.get('country')
        x.pinCode = requests.POST.get('pinCode')
        x.image = requests.FILES.get('myImg')
        x.save()
    return render(requests,'update.html',{'user':user, 'requests':requests})

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
