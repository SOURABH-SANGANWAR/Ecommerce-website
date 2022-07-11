from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def myCart(requests):
    if not requests.user.is_authenticated:
        return redirect('login_page')
    x = requests.user.MyOrders.get(is_cart  = True)
    print(x)
    product  = x.products.all()
    print(product)
    totalValue = 0
    for i in product:
        totalValue+=(i.Quantity)*(i.Seller.Price)
    x.netPrice = totalValue
    x.save()
    if requests.method =='POST':
        if 'delete' in requests.POST:
            for i in product:
                if requests.POST.get(str(i.Seller.id)):
                    requests.user.MyOrders.get(is_cart  = True).products.remove(i)
                    return redirect('/cart')
        elif 'Checkout' in requests.POST:
            x.is_cart = False
            x.save()
            x = requests.user.MyOrders.create(netPrice = 0,customer = requests.user)
            return redirect('/cart')
        else:
            for i in product:
                if requests.POST.get(str(i.Seller.id)):
                    i.Quantity = requests.POST.get(str(i.Seller.id))
                    i.save()
                    return redirect('/cart')
    return render(requests,'cart.html',{'products': product,'order':x, '10r':range(1,10), 'requests':requests})

@login_required
def myOrder(requests, id = None):
    if not id:
        return HttpResponse('<h2>Record Not Found</h2>')
    
    try:
        if not requests.user.is_authenticated:
            return redirect('/login_page')
        x = requests.user.MyOrders.get(id = id)
        print(x)
        print('hello')
        if x.is_cart:
            print(x.is_cart)
            raise 
        
        totalValue = 0
        product  = x.products.all()
        for i in product:
            totalValue+=(i.Quantity)*(i.Seller.Price)
        x.netPrice = totalValue
        x.save()
        netValue = 0
        print('hai')
        return render(requests,'OrderDetail.html',{'products': product,'order':x, '10r':range(1,10), 'requests':requests})
    except:
        return HttpResponse('<h2>Access Denied</h2>')


@login_required
def myOrderList(requests):
    orders = requests.user.MyOrders.exclude(is_cart  = True)
    # orders = requests.user.MyOrders.all()
    print(orders)
    if requests.user.is_authenticated:
        print("logged in")
    return render(requests,'OrderList.html',{'orders':orders, 'requests':requests})