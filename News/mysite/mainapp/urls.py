from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('category/<int:category_id>/', view_category, name="category"),
    path('news/<int:news_id>/', view_news, name="view_news"),
    path('weather/', weather, name="weather"),
    path('add_news/', add_news, name="add_news"),
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),

]

