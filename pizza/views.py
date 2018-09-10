from django.shortcuts import render, HttpResponse

def homepage(request):
    context = {}
    return render(request, "homepage.html", context)