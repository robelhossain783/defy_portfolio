from django.shortcuts import render, redirect


def home(request):
    return render(request, "test.html")

def contract(request):
    return render(request, "contact_2.html")
