import products
from django.shortcuts import render
from .models import Product
# Create your views here.


def home(request):
    card = Product.objects.all()
    return render(request, 'home.html', {'card': card})


def our_prouducts(request):
    products = Product.objects.count
    card = Product.objects.all()
    return render(request, 'products.html', {'products': products, 'card': card})


def order_buy(request, order_id):
    order = Product.objects.get(pk=order_id)
    return render(request, 'order.html', {'order': order})


def privacy(request):
    return render(request, 'privacy_policy.html', {})


def refund(request):
    return render(request, 'refund_policy.html', {})


def contact_us(request):
    return render(request, 'contact_us.html', {})
