from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("HOME 2")


def contact(request):
    return HttpResponse("Contact")


def about(request):
    return HttpResponse("About")
