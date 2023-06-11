from django.shortcuts import render, get_object_or_404
from .models import Item
from core.models import Order, Order_Item, User
# from django.contrib.auth.models import User

# Create your views here.
def detail(request, pk):

    item = get_object_or_404(Item, pk=pk)
    customer = User.objects.filter(username=request.user.username)[0]
    order = Order.objects.filter(user = customer)[0]

    related_items = Item.objects.filter(category = item.category).exclude(pk=pk)[0:3]

    a = dict()
    
    if request.method == 'POST':
        order_item = Order_Item(order = order, item = item)
        order_item.save()
        items = Order_Item.objects.filter(order=order)
        a['items'] = items
        return render(request, 'core/cart.html',context=a)
    
    a['item'] = item
    a['related_items'] = related_items

    order_item = Order_Item.objects.filter(order=order, item=item)

    if order_item.exists():
        a['bought'] = True
    else:
        a['bought'] = False
    
    return render(request, 'item/detail.html',context=a)