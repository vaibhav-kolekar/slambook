from django.shortcuts import render, HttpResponse
from .models import sai
# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        honest = request.POST.get('honest')
        rel = request.POST.get('rel')
        impression = request.POST.get('impression')
        memory = request.POST.get('memory')
        friend = request.POST.get('a1')
        colour = request.POST.get('v1')
        chara = request.POST.get('b1')
        quality = request.POST.get('c1')
        emotional = request.POST.get('d1')
        sev = sai(name = name, honest = honest, rel = rel, impression = impression, memory = memory, friend = friend, colour = colour, chara = chara, quality = quality, emotional = emotional)
        sev.save()

    return render(request, 'home.html')