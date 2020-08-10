from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from store.models import Product,Order
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'store/store.html'
    ordering = ['-date']

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(UserPassesTestMixin, CreateView):
    model = Product
    fields = ['image','title','price','about','discription']

    def test_func(self):
        return self.request.user.is_superuser

class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['image','title','price','about','discription']

    def test_func(self):
        return self.request.user.is_superuser

# function for Cart
@login_required
def cart(request):
    return render(request,'store/cart.html')

@login_required
def createOrder(request,pk):
    product = Product.objects.get(pk=pk)
    order, created = Order.objects.get_or_create(product=product, customer=request.user)
    return redirect('store')

@login_required
def updateQuantity(request):
    data = json.loads(request.body)
    orderId = data['orderId']
    action = data['action']

    order = Order.objects.get(id=orderId)

    if action=='add':
       order.quantity = order.quantity + 1
    elif action=='remove':
       order.quantity = order.quantity - 1

    order.save()

    if order.quantity <= 0:
       order.delete()

    return JsonResponse('fetching is complete', safe=False)

@login_required
def checkOut(request):
    return render(request,'store/checkOut.html')
