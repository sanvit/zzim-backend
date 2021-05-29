from zzim.models import item, shoppingMall
from urllib.parse import urlparse, parse_qs
import requests
from bs4 import BeautifulSoup


def parser(url):
    if "mitem" in url:
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')
        name = soup.find('div',{'class':'box__item-title'}).find('h3').text
        price_str = soup.find('span',{'class':'text__price'}).find('span',{'class':'text_number'}).text
        price = ""
        for c in price_str:
            if c.isdigit():
                price = price + c
        if price == "":
            price = 0
        else:
            price = int(price)

        shipping_str = soup.find('span',{'class':'text__branch'}).text
        shipping = ""
        for c in shipping_str:
            if c.isdigit():
                shipping = shipping + c
        if shipping == "":
            shipping = 0
        else:
            shipping = int(shipping)
        image_url = soup.find('meta', {'property': 'og:image'}).get('content')
        new_item = item()
        new_item.name = name
        new_item.price = price
        new_item.shipping = shipping
        new_item.mall = shoppingMall.objects.get(slug='gmarket')
        new_item.url = url
        new_item.image_url = image_url
        new_item.save()
        return new_item
    request = requests.get(url)
    print(url)
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
    shipping_str = soup.find_all('div', {'class': 'box__information'})[1].text.split('원')
    shipping_str = shipping_str[0]
    shipping = ""
    for c in shipping_str:
        if c.isdigit():
            shipping = shipping + c
    if shipping == "":
        shipping = 0
    else:
        shipping = int(shipping)
    image_url = soup.find('meta', {'property': 'og:image'}).get('content')

    # 모델에 저장
    new_item = item()
    new_item.name = name
    new_item.price = price
    new_item.shipping = shipping
    new_item.mall = shoppingMall.objects.get(slug='gmarket')
    new_item.url = url
    new_item.image_url = image_url
    new_item.save()
    return new_item
