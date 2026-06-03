import time

from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def ping1(request):
    return JsonResponse({"message": f"pong {time.time()}"})
