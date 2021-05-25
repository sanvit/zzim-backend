from zzim.models import item, shoppingMall
from urllib.parse import urlparse, parse_qs
from .auction import parser as auctionparser
from .sk11st import parser as sk11stparser
from .naver import parser as naverparser
from .gmarket import parser as gmarketparser


def itemUrlParser(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if "gmarket" in domain:
        item_object = gmarketparser(url)
    elif "11st" in domain:
        item_object = sk11stparser(url)
    elif "naver" in domain:
        item_object = naverparser(url)
    elif "auction" in domain:
        item_object = auctionparser(url)
    return item_object
