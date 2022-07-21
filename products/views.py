from unicodedata import category
from django.shortcuts import render,get_object_or_404,redirect
# from Cus.models import Account
from .models import Product,Category,Product_Seller, Varient
from django.views import View
from .forms import RegisterProduct
from django.urls import reverse
from nltk.stem import PorterStemmer

from django.contrib.auth.decorators import login_required
# Create your views here.
def detail_view(requests,id, seller = None):
    x = Product.objects.get(id = id)
    k = Product.objects.filter(category = x.category)
    z= x.Sellers.all()
    mp = x.Price
    try:
        c_seller = x.Sellers.get(Price = mp)
    except:
        c_seller = x.Sellers.all()[0]
        mp = c_seller.Price
    if(seller):
        c_seller = x.Sellers.get(id = seller)
        mp = c_seller.Price
    context = {
        'objects' : Product.objects.filter(Name = x.Name),
        'obj' : x, 
        'ranges' : range(5), 
        'varients' :False, 
        'colours': x.Colours.all(), 
        'discount':(x.MRP-x.Price)*100//x.MRP, 
        'ratings' : x.Rating , 
        'reviews': x.Reviews.all(), 
        'sellers': x.Sellers.exclude(id = c_seller.id), 
        'Nsellers': len(z),  
        'bestPrice': mp,
        'login': True,
        'Similiar': k,
        'c_seller' : c_seller,
        'Simlen':(len(k)+1)*230,
        'ids':f'/products/{id}/',
        'requests':requests
        }
    print(context['ids'])
    context['varients'] = bool(len(context['objects'])-1)
    if requests.method == 'POST':
        print("yes")
        if(requests.user.is_authenticated):
            myc = requests.user.MyOrders.get(is_cart  = True)
            allcartprodts  = requests.user.MyOrders.get(is_cart  = True).products.all()
            for i in allcartprodts:
                if i.Seller == c_seller:
                    return redirect('Products:detail_view_seller',id = x.id,seller = c_seller.id)        
            myc.products.create(Item = x,Seller = c_seller,Quantity = 1)
            
            return redirect('/cart')
    return render(requests,'view.html',context)

def detail_view_Category(requests,id):
    filtered = Category.objects.get(id = id).product_set.all()
    filtered = Product.objects.all()
    print(filtered)
    cats = Category.objects.all()
    return render(requests,'Product_list.html',{'prods':filtered, 'desc':'Search Results:','cats':cats,'requests':requests})

def search(requests,search = None,id1 = None,id = None):
    if(search!=None):
        ps = PorterStemmer()
        lists = [ps.stem(w) for w in search.split(" ")]
        print(lists)
        b  =[]
        for i in lists:
            b.append(Product.objects.filter(Name__contains = i))#description__contains = i,
        for i in search.split(" "):
            b.append(Product.objects.filter(Name__contains = i))#description__contains = i, 
        filtered = b[0]
        for i in b:
            filtered  =filtered | i
    else:
        filtered = Product.objects.all()
        print(filtered)
    if(id1!=None):
        filtered = filtered.filter(category__id = id1)
        print('cats\n\n\n')
        print(filtered)
    if(id!=None):
        filtered = filtered.filter(category__id = id)
        print('cats\n\n\n')
        print(filtered)
    cats = Category.objects.all()
    if requests.method =='POST':
        if 'category' in requests.POST:
            if(search):
                return  redirect('Products:search_filter',search=search, id1 = requests.POST.get('cats'))
            else:
                return  redirect('Products:detail_view_filter',id = requests.POST.get('cats'))
        elif 'search' in requests.POST:
            return  redirect('Products:search_filter',search=requests.POST.get('search'), id1 = id1)
    filtered = filtered.filter(is_root = True)
    return render(requests,'Product_list.html',{'prods':filtered, 'desc':'Search Results:','cats':cats,'requests':requests})


@login_required
def addv(requests, id = None):
    if(id == None):
        return redirect('Products:create_view')
    if(not( requests.user.is_seller or requests.user.is_staff)):
            return redirect("Products:search")
    x = Product.objects.get(id = id)
    if(x == None):
        return redirect('Products:create_view')
    if requests.method == 'POST':
        q = Varient.objects.get(Name = requests.POST.get('Varient')).id
        if(q!=None):
            print('Varient exisits')
            z = Product.objects.filter(Name = x.Name).filter(Varients_id = q)
            if z:
                y = z[0]
                print('Product with This varient exisits')
                print(requests.user)
                print(y.Sellers.all())
                for sellers in y.Sellers.all():
                    print(sellers.Name, requests.user)
                    if requests.user == sellers.Name:
                        print('yes')
                        return render(requests, 'addv.html', {'requests' : requests, 'obj': x, 'msg': 'Already selling this product you can click on update price.'})
            else:
                y = Product.objects.create(Name = x.Name, Image = x.Image, Price = requests.POST.get('Price'), MRP = requests.POST.get('MRP'),  description  = x.description, features = x.features, category = x.category, varient_desc = x.varient_desc, Product_tags = x.Product_tags)
                y.save()
                y.Colours.add(*x.Colours.all());
                y.is_root = False
                y.save()
            y.Sellers.create(Name = requests.user, Price = y.Price)
            y.save()
        else:    
            y = Product.objects.create(Name = x.Name, Image = x.Image, Price = requests.POST.get('Price'), MRP = requests.POST.get('MRP'),  description  = x.description, features = x.features, category = x.category, varient_desc = x.varient_desc, Product_tags = x.Product_tags)
            y.save()
            y.Colours.add(*x.Colours.all());
            y.Sellers.create(Name = requests.user, Price = y.Price)
            y.Varients= Varient.objects.create(Name = requests.POST.get('Varient'))
            y.is_root = False
            y.save()
        return redirect('Products:detail_view', id = y.id)
    return render(requests, 'addv.html', {'requests' : requests, 'obj': x, 'msg': None})


class cview(View):
    def get(self,requests,id=None,*args, **kwargs):
        print(requests.user)
        if(not (requests.user.is_authenticated )):
            return redirect("Products:search")
        if(not( requests.user.is_seller or requests.user.is_staff)):
            return redirect("Products:search")
        obj = None
        if id is not None:
            obj = get_object_or_404(Product,id = id)
        else:
            forms = RegisterProduct()
        if obj is not None:
            forms = RegisterProduct(instance=obj)
        context = {'form':forms,'obj':obj,'requests':requests}
        print(obj)
        return render(requests,'create.html',context)
    def post(self,requests,id=None,*args, **kwargs):
        if(not requests.user.is_authenticated):
            return redirect("Products:search")
        if(not( requests.user.is_seller or requests.user.is_staff)):
            return redirect("Products:search")
        obj = None
        if id is not None:
            obj = get_object_or_404(Product,id = id)
        else:
            forms = RegisterProduct(requests.POST, requests.FILES)
            if forms.is_valid():
                x = forms.save()
                y = Product_Seller.objects.create(Name = requests.user, Price = x.Price)
                x.Sellers.add(y)
                x.save()
                return redirect('Products:detail_view',id = x.id)
                forms = RegisterProduct()
        if obj is not None:
            forms = RegisterProduct(requests.POST, requests.FILES, instance=obj)
            if forms.is_valid():
                print(requests.POST)
                if 'Save' in requests.POST:
                    forms.save()
                else:
                    return redirect("products:delete_view",id= id)    
                return redirect("products:detail_view",id= id)
        context = {'form':forms,'obj':obj,'requests':requests}
        return render(requests,'create.html',context)

# class lview(View):
#     def get(self,requests,*args, **kwargs):
#         obj = data.objects.all()
#         context = {'objects':obj,'create':reverse("products:create_view")}
#         return render(requests,'lisst.html',context)
#     # def post(self,requests,*args, **kwargs):
#     #     obj = data.objects.all()
#     #     context = {'objects':obj}
#     #     if 'create' in requests.post:
#     #         return redirect("products:create_view")
#     #     return render(requests,'list.html',context)

# class dview(View):
#     def get(self,requests,id=None,*args, **kwargs):
#         if(not requests.user.is_authenticated):
#             return redirect("products:list_view")
#         obj  = get_object_or_404(data,id = id)
#         return render(requests,'delete.html',{'obj':obj})
#     def post(self,requests,id=None,*args, **kwargs):
#         if(not requests.user.is_authenticated):
#             return redirect("products:list_view")
#         value = id
#         obj  = get_object_or_404(data,id = id)
#         if 'yes' in requests.POST:
#             obj.delete()
#             return redirect("products:list_view")
#         if 'no' in requests.POST:
#             return redirect("products:detail_view",id= value)
#         return render(requests,'delete.html',{'obj':obj})

