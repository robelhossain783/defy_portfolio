from django.urls import path
from portfolio.view.home import home

urlpatterns = [
    path("", home, name="home"),

]