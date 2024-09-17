from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def index(request, qtd_posts):
    res = []

    for i in range(1, qtd_posts):
        res.append("a"+"1")

    return JsonResponse(res, safe=False)