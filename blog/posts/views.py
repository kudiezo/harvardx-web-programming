from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def index(request, qtd_posts):
    res = []

    for i in range(qtd_posts-9, qtd_posts+1):
        res.append(i)

    return JsonResponse(res, safe=False)