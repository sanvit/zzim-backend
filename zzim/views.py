from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .parsers import *
from .models import *
from user.models import User
from urllib.parse import urlparse
# Create your views here.


def listItem(req):
    user = req.user
    items = user.item_set.all()
    item_list = []
    for i in items:
        item_json = {'id': i.uuid, 'image': i.image_url, 'name': i.name, 'price': i.price,
                     'shippingPrice': i.shipping, 'shoppingMallName': i.mall.name, 'logoImage': i.mall.logo,
                     'createdDate': i.date_added, 'url': i.url}
        item_list.append(item_json)
    return JsonResponse({"status": "SUCCESS", "data": item_list})


def viewItem(req, id):
    item_object = get_object_or_404(item, pk=id)
    if req.user == item_object.user or req.user.is_public:
        return JsonResponse(
            {'image': item_object.image_url, 'name': item_object.name, 'price': item_object.price,
             'shippingPrice': item_object.shipping, 'shoppingMallName': item_object.mall.name,
             'logoImage': item_object.mall.logo, 'createdDate': item_object.date_added, 'url': item_object.url})
    return JsonResponse({"status": "FAILED", "message": "사용자 정보가 일치하지 않습니다."}, status=403)


def editItem(req, id):
    item_object = get_object_or_404(item, pk=id)
    if req.user == item_object.user:
        if req.method == 'POST':
            item_object.name = req.POST['name']
            item_object.price = req.POST['price']
            item_object.shipping = req.post['shipping']
            item_object.save()
            return JsonResponse({"status": "SUCCESS", "message": "성공적으로 수정되었습니다."})
        return JsonResponse({'image': item_object.image_url, 'name': item_object.name, 'price': item_object.price,
                             'shippingPrice': item_object.shipping, 'logoImage': item_object.mall.logo,
                             'createdDate': item_object.date_added, 'url': item_object.url})
    return JsonResponse({"status": "FAILED", "message": "사용자 정보가 일치하지 않습니다."}, status=403)


def setPurchasedItem(req, id):
    item_object = get_object_or_404(item, pk=id)
    if req.user == item_object.user:
        item_object.is_purchased == True
        item_object.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=403)


def deleteItem(req, id):
    item_object = get_object_or_404(item, pk='id')
    if req.user == item_object.user:
        item_object.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=403)


def addItem(req):
    if req.method == "POST":
        url = req.POST['url']
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if "gmarket" in domain:
            item_object = gmarket.parser(url)
#        elif "11st" in domain:
#            item_object = 11st.parser(url)
        elif "naver" in domain:
            item_object = naver.parser(url)
        elif "auction" in domain:
            item_object = auction.parser(url)
        else:
            return JsonResponse({'status': 'FAILED', 'message': '현재 지원하지 않는 쇼핑몰입니다.'}, status=400)


def viewOtherUserItem(req, id):
    user = get_object_or_404(User, username=id)
    print('#')
    if user.is_public:
        items = user.item_set.all()
        item_list = []
        for i in items:
            item_json = {'id': i.uuid, 'image': i.image_url, 'name': i.name, 'price': i.price,
                         'shippingPrice': i.shipping, 'shoppingMallName': i.mall.name, 'logoImage': i.mall.logo,
                         'createdDate': i.date_added, 'url': i.url}
            item_list.append(item_json)
        return JsonResponse({"status": "SUCCESS", "nickname": user.nickname, "data": item_list})
    return JsonResponse({"status": "FAILED", "message": "비공개 프로필입니다."}, status=403)
