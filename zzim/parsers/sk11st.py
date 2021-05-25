from urllib.parse import urlparse, parse_qs
import requests
from bs4 import BeautifulSoup
from zzim.models import item, shoppingMall


def parser(url):
    #    prdNo = parse_qs(urlparse(url).query).get('prdNo')[0]\
    #    pcurl = f"http://www.11st.co.kr/products/{prdNo}"
    #    print(url)
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    name = soup.find('h1', {'class': 'title'}).text
    price_str = soup.find('span', {'class': 'value'}).text
    price = ""
    for c in price_str:
        if c.isdigit():
            price = price + c
    if price == "":
        price = 0
    else:
        price = int(price)
    shipping_str = soup.find('div', {'class': 'delivery'}).find('dt').text
    shipping = ""
    for c in shipping_str:
        if c.isdigit():
            shipping = shipping + c
    if shipping == "":
        shipping = 0
    else:
        shipping = int(shipping)

    image_url = soup.find('meta', {'property': 'og:image'}).get('content')
    print(price)
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
