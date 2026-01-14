from django.urls import path
from portfolio.view.home import home, contract
from portfolio.view.my_home import my_home, download_cv, find_me, services
urlpatterns = [

    path("", my_home, name="my_home"),
    path("contact/", contract, name="contact"),
    path('download-cv/', download_cv, name='download_cv'),
    path('find_me/', find_me, name='find_me'),
    path('services/', services, name='services'),

]