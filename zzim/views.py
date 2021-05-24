from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from urllib.parse import urlparse
from parsers import *

# Create your views here.

def setPurchaseItem(request, id):
    item_object = get_object_or_404(item, pk='id')
    if request.user == item_object.user:
        item_object.is_purchased == True
        return JsonResponse({'status':'success'})
    return JsonResponse({'status':'fail'})

def deleteItem(request, id):
    item_object = get_object_or_404(item, pk='id')
    if request.user == item_object.user:
        item_object.delete()
        return JsonResponse({'status':'success'})
    return JsonResponse({'status':'fail'})

def shareItem(request,id):
    item_object = get_object_or_404(item,pk='id')
    if request.user == item_object.user:
        item_object.is_shared =True
        return JsonResponse({'status':'success'})
    return JsonResponse({'status':'fail'})

def addItem(request):
    if request.method == "POST":
        url = request.POST['url']
        parsed_url = urlparse(url)
        if "gmarket" in urlparse(url).netloc:
            item_object = gmarket.parser(url)
        elif "11st" in urlparse(url).netloc:
            item_object = 11st.parser(url)
        elif "naver" in urlparse(url).netloc:
            item_object = naver.parser(url)
        elif "auction" in urlparse(url).netloc:
            item_object = auction.parser(url)
        