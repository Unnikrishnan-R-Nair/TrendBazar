from django.shortcuts import render, redirect

from django.views.generic import View

from store.forms import RegistrationForm, LoginForm

from django.contrib.auth import authenticate, login, logout

from store.models import Product, Size, BasketItem

# Create your views here.


class SignUpView(View):

    def get(self, request, *args, **kwargs):

        form = RegistrationForm()

        return render(request, "register.html", {"form": form})
    
    def post(self, request, *args, **kwargs):

        form = RegistrationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("signin")
        
        return render(request, "login.html", {"form": form})


class SignInView(View):

    def get(self, request, *args, **kwargs):

        form = LoginForm()

        return render(request, 'login.html', {'form': form})
    
    def post(self, request, *args, **kwargs):

        form = LoginForm(request.POST)

        if form.is_valid():

            uname = form.cleaned_data.get('username')

            pwd = form.cleaned_data.get('password')

            user_object = authenticate(request, username=uname, password=pwd)

            if user_object:

                login(request, user_object)

                return redirect('home')
            
        return render(request, 'login.html', {'form': form})
    
    
    
class HomeView(View):

    def get(self, request, *args, **kwargs):

        qs = Product.objects.all()

        return render(request, 'home.html', {'data': qs})
    

    
class ProductDetailView(View):

    def get(self, request, *args, **kwargs):

        id = kwargs.get('pk')

        qs = Product.objects.get(id=id)

        return render(request, 'product_detail.html', {'data': qs})
    


# url : localhost:8000/products/{id}/carts/add/

class AddToCartView(View):

    def post(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')

        product_obj = Product.objects.get(id=id)

        size_name = request.POST.get('size')

        size_obj = Size.objects.get(name=size_name)

        basket_obj = request.user.cart 

        BasketItem.objects.create(

            basket_object=basket_obj,
            product_object=product_obj,
            size_object=size_obj

        )

        return redirect('cart-list')
    


class CartItemListView(View):

    def get(self, request, *args, **kwargs):

        qs = request.user.cart.cartitems.filter(is_order_placed=False)

        return render(request, 'cart_items.html', {'data': qs})
    


# url: localhost:8000/basket/items/{id}/remove/
    
class BasketItemDeleteView(View):

    def get(self, request, *args, **kwargs):

        basket_item_object = BasketItem.objects.get(id=kwargs.get('pk'))

        basket_item_object.delete()

        return redirect('cart-list')
    


# url : localhost:8000/basket/item/{id}/quantity/change/
    
class BasketItemUpdateQuantityView(View):

    def post(self, request, *args, **kwargs):

        id = kwargs.get('pk')

        basket_item_obj = BasketItem.objects.get(id=id)

        # print(request.POST.get('action')) # dec or inc

        action = request.POST.get('action')

        if action == 'inc':

            basket_item_obj.quantity += 1
        
        elif action == 'dec':

            basket_item_obj.quantity -= 1

        basket_item_obj.save()


        return redirect('cart-list')
    

    
class CheckOutView(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'checkout.html')
    
    