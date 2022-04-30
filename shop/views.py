from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .models import Category, Product

# Create your views here.
categories = Category.objects.values('id', 'title', 'slug')
products = Product.objects.values('id', 'title', 'slug', 'price', 'image', 'sale')


def index(request):
    return render(
        request,
        "index.html",
        {
            "categories": categories,
            "products": products,
            "home_page": "active",
        },
    )


def shop(request):
    paginator = Paginator(products, 12)
    page = request.GET.get("page")
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        "products": paged_products,
        "product_count": product_count,
        "store_page": "active",
        "categories": categories,
    }

    return render(request, "shop.html", context)


def about(request):
    return render(
        request, "about.html", {"categories": categories, "about_page": "active"}
    )


def contact(request):
    return render(
        request, "contact.html", {"categories": categories, "contact_page": "active"}
    )


def detail(request, slug):
    single_product = Product.objects.get(slug=slug)
    return render(
        request,
        "shop-single.html",
        {
            "categories": categories,
            "single_product": single_product,
            "store_page": "active",
        },
    )

def thankyou(request, slug, slug1):
    single_product = Product.objects.get(slug=slug1)

    return render(request, "thankyou.html", {"categories": categories, "single_product": single_product})

def search(request):
    if "keyword" in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            products = Product.objects.filter(title__icontains=keyword)
            product_count = products.count()
    context = {
        "products": products,
        "product_count": product_count,
        "store_page": "active",
        "categories": categories,
    }
    return render(request, "shop.html", context)

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("login")

    return render(request, "login.html")

def logout_page(request):
    logout(request)
    return redirect("index")

def signup_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass"]
        
        if username not in User.objects.all():
            User.objects.create_user(username=username, password=password)
            return redirect("login")
        else:
            return redirect("signup")
    else:
        return render(request, "register.html")


