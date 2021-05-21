from zzim.models import item, shoppingMall
from urllib.parse import urlparse, parse_qs
import requests
from bs4 import BeautifulSoup


def parser(url):
    itemno = ""
    if parse_qs(urlparse(url).query).get('itemno'):
        itemno = parse_qs(urlparse(url).query).get('itemno')
    elif parse_qs(urlparse(url).query).get('itemNo'):
        itemno = parse_qs(urlparse(url).query).get('itemNo')
    else:
        itemno = parse_qs(urlparse(url).query).get('ItemNo')

    url = f"http://itempage3.auction.co.kr/DetailView.aspx?itemno={itemno[0]}"
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    name = soup.find('h1', {'class': 'itemtit'}).text
    price_str = soup.find('strong', {'class': 'price_real'}).text
    price = ""
    for c in price_str:
        if c.isdigit():
            price = price + c
    if price == "":
        price = 0
    else:
        price = int(price)
    shipping_str = soup.find('button', {'id': 'ucShippingInfo_btnShippingInfoTitleText'}).text
    shipping = ""
    for c in shipping_str:
        if c.isdigit():
            shipping = shipping + c
    if shipping == "":
        shipping = 0
    else:
        shipping = int(shipping)
    # 모델에 저장
    new_item = item()
    new_item.name = name
    new_item.price = price
    new_item.shipping = shipping
    new_item.mall = shoppingMall.objects.get(slug='auction')
    new_item.url = url
    new_item.item_no = itemno
    new_item.save()
