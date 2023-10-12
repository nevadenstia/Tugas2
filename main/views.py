from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

@login_required(login_url='/login')

def show_main(request):

    products = Product.objects.filter(user=request.user)
    # Check if 'last_login' exists in request.COOKIES and set a default value if not found
    last_login = request.COOKIES.get('last_login', 'N/A')
    context = {
        'name' : request.user.username,
        'npm' : '2206083073',
        'kelas' : 'PBP B',
        'products' : products,
        'last_login' : last_login,
    }

    return render(request, "main.html", context)

def get_total_stock(request):
    total_stock = Product.objects.filter(user=request.user).aggregate(total_stock=Sum('amount'))['total_stock'] or 0
    return JsonResponse({'total_stock': total_stock})


def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        item_name = request.POST.get("item_name")
        image = request.POST.get("image")
        amount = request.POST.get("amount")
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        reviews = request.POST.get('reviews')
        user = request.user

        new_product = Product(item_name=item_name, image=image, amount=amount, description=description, rating=rating, reviews=reviews, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

# Fungsi untuk menambah amount suatu objek sebanyak satu
@csrf_exempt
def add_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Product, id=item_id)
        item.amount += 1
        item.save()
    return HttpResponse

# Fungsi untuk mengurangi jumlah stok suatu objek sebanyak satu
@csrf_exempt
def subtract_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Product, id=item_id)
        if item.amount > 0:
            item.amount -= 1
            item.save()
    return HttpResponse

# Fungsi untuk menghapus suatu objek dari inventori
@csrf_exempt
def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Product, id=item_id)
        item.delete()
    return HttpResponse


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")