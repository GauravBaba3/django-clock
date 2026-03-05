from django.shortcuts import render
import time

def home(request):
    data = {
        "title": "Digital clock",
    }
    time.sleep(5)
    return render(request, "home/home.html", data)