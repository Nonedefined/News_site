from django.core.paginator import Paginator
from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import *
from .forms import *


def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        news = News.objects.filter(title__icontains=search_query, is_published=True)
    else:
        news = News.objects.filter(is_published=True)

    categories = Category.objects.all()
    paginator = Paginator(news, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)

    context = {"page_obj": page_objects, "categories": categories, "title": "News list"}
    return render(request, "mainapp/index.html", context)


def view_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Exception:
        return render(request, "mainapp/page_not_found.html")

    news = News.objects.filter(is_published=True, category_id=category_id)
    paginator = Paginator(news, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)

    categories = Category.objects.all()
    context = {"page_obj": page_objects, "categories": categories, "category": category, "title": category.title}

    return render(request, "mainapp/category.html", context)


def view_news(request, news_id):
    try:
        news = News.objects.get(pk=news_id, is_published=True)
    except Exception:
        return render(request, "mainapp/page_not_found.html")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            Comment.objects.create(text=text, user=request.user, news=news)
            return redirect(news)
    else:
        form = CommentForm()

    categories = Category.objects.all()
    comments = Comment.objects.filter(news=news)
    context = {"news": news, "categories": categories, "form": form, "comments": comments, "title": news.title}

    return render(request, "mainapp/view_news.html", context)


def weather(request):
    weather_cities = WeatherCity.objects.all()
    "{city}"

    categories = Category.objects.all()
    context = {"categories": categories, "weather_cities": weather_cities, "title": "weather"}
    return render(request, "mainapp/weather.html", context)


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your news has been sent for review")
            return redirect("home")
    else:
        form = NewsForm()

    categories = Category.objects.all()
    context = {"categories": categories, "form": form, "title": "Suggest news"}
    return render(request, "mainapp/add_news.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Successful registration")
            return redirect("home")
        else:
            messages.error(request, "Registry error")
    else:
        form = UserRegisterForm()

    return render(request, "mainapp/register.html", {"form": form, "title": "Registration"})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "mainapp/login.html", {"form": form, "title": "Authorization"})


def user_logout(request):
    logout(request)
    return redirect("login")

