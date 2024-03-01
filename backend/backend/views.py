from django.shortcuts import render
from django.http import JsonResponse

def getRouters(request):
    return JsonResponse("helloooo", safe=False)