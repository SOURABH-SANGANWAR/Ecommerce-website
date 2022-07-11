from django.shortcuts import render,get_object_or_404,redirect
# from Cus.models import Account
from .models import Product,Category
from django.views import View
# from .forms import MakeForm
from django.urls import reverse
from nltk.stem import PorterStemmer

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
        b  =[]
        for i in lists:
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






# class cview(View):
#     def get(self,requests,id=None,*args, **kwargs):
#         if(not (requests.user.is_authenticated and requests.user.is_staff)):
#             return redirect("products:list_view")
#         obj = None
#         if id is not None:
#             obj = get_object_or_404(Product,id = id)
#         else:
#             forms = MakeForm()
#         if obj is not None:
#             forms = MakeForm(instance=obj)
#         context = {'form':forms,'obj':obj}
#         print(obj)
#         return render(requests,'new.html',context)
#     def post(self,requests,id=None,*args, **kwargs):
#         if(not requests.user.is_authenticated):
#             return redirect("products:list_view")
#         obj = None
#         if id is not None:
#             obj = get_object_or_404(data,id = id)
#         else:
#             forms = MakeForm(requests.POST)
#             if forms.is_valid():
#                 forms.save()
#                 forms = MakeForm()
#         if obj is not None:
#             forms = MakeForm(requests.POST, instance=obj)
#             if forms.is_valid():
#                 print(requests.POST)
#                 if 'Save' in requests.POST:
#                     forms.save()
#                 else:
#                     return redirect("products:delete_view",id= id)    
#                 return redirect("products:detail_view",id= id)
#         context = {'form':forms,'obj':obj}
#         return render(requests,'new.html',context)

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

