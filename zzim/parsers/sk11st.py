from urllib.parse import urlparse, parse_qs
import requests
from bs4 import BeautifulSoup
from zzim.models import item, shoppingMall


def parser(url):
    prdNo = ""
    if "prdNo"in url:
        prdNo = url.split('=')[1]
        if '&' in prdNo:
            prdNo = prdNo.split('&')[0]
        url = "http://www.11st.co.kr/products/"+prdNo
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    name = soup.find('h1', {'class': 'title'}).text
    price_str = soup.find('dl', {'class': 'price'}).find('span', {'class': 'value'}).text
    price = ""
    for c in price_str:
        if c.isdigit():
            price = price + c
    if price == "":
        price = 0
    else:
        price = int(price)
    shipping_str = soup.find('div',{'class':'delivery'})
    if(shipping_str==None):
        shipping_str = soup.find('div',{'class':'delivery_abroad'})
    shipping_str = shipping_str.find('strong').text
    if "개당" in shipping_str:
        shipping_str = shipping_str.split("개당")[1]
    shipping = ""
    for c in shipping_str:
        if c.isdigit():
            shipping = shipping + c
    if shipping == "":
        shipping = 0
    else:
        shipping = int(shipping)

    image_url = soup.find('meta', {'property': 'og:image'}).get('content')
    name = name.strip()

    # 모델에 저장
    new_item = item()
    new_item.name = name
    new_item.price = price
    new_item.shipping = shipping
    new_item.mall = shoppingMall.objects.get(slug='11st')
    new_item.url = url
    new_item.image_url = image_url
    new_item.save()
    return new_item
