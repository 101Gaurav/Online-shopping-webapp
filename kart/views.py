from django.shortcuts import render,redirect
from kart.models import Items,Order
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def index(request):

    items=Items.objects.all()

    return render(request,"index.html",{"items":items})

def product(request):
    temp=list(request.GET.keys())
#    cart=Cart()
    try:
        item=Items.objects.get(name=temp[0])
    except ObjectDoesNotExist:
        return HttpResponse("Products does not exist")
    return render(request,"product.html",{"item":item})


def add_to_cart(request):
    temp = list(request.GET.keys())
    #    cart=Cart()
    try:
        if request.user.is_authenticated:
            item = Items.objects.get(id=temp[0])
            print("item = ",item.name)
            order=Order(owner=request.user)
            print("added owner", order.owner.username)
            order.save()
            order.product.add(item)
            order.save()
            print("added product",order.product.name)
            cart_item=Order.objects.filter(owner=request.user,is_ordered=False)
            for i in cart_item:
                print(i.product)
                print(i.owner)
            return render(request,"product.html",{"cart_item":cart_item,"item":item})
        else:
            return redirect("/")

    except ObjectDoesNotExist:
        return HttpResponse("Products does not exist")


#    return render(request, "product.html", {"item": item, 'temp': temp[0]})


#        print(item)


def cart(request):

    all_order = Order.objects.filter(owner=request.user,is_ordered=False)
    order=Order()
    total = order.get_cart_total()
    print(total)

    return render(request, "cart.html", {"all_order": all_order, "total": total})
#    return render(request, "cart.html")


def item_delete(request):
    temp = list(request.GET.keys())
    Order.objects.filter(id=temp[0]).delete()
    print("Item deleted",Order.objects.filter(id=temp[0]).product.name)
    cart(request)

'''
    if request.method == "POST":
        return render(request , "cart.html")
    else:
        return redirect("/")
'''