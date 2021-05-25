from zzim.models import item
import requests
from bs4 import BeautifulSoup


def parser(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    new_item = item()

    name = soup.find('h3', {'class': '_3oDjSvLwq9 _copyable'}).text
    new_item.name = name

    price = soup.find('span', {'class': '_1LY7DqCnwR'}).text
    new_item.price = int(price.replace(",", ""))

    is_moobae = soup.find('span', {'class': 'Y-_Vd4O6dS'}).text
    if(is_moobae == "무료배송"):
        shipping = 0
    else:
        shipping = soup.find('span', {'class': 'Y-_Vd4O6dS'}).find('span', '_1_wrVRMvuL').text
    new_item.shipping = shipping.replace(",", "")

    new_item.mall = '네이버 스마트스토어'

    new_item.image_url = soup.find('div', {'class': '_23RpOU6xpc'}).find('img')['src']

    new_item.save()
    return new_item
