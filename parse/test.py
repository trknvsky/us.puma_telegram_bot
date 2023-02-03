import requests
from bs4 import BeautifulSoup
from decimal import Decimal

cgid = 'mens-shoes'

url = 'https://us.puma.com/on/demandware.store/Sites-NA-Site/en_US/Search-UpdateGrid'
params = {
        'cgid': cgid,
        'start': 0,
        'sz': 2000,
        'isAjax': 1
    }
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
            'AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 39.0.2171.95Safari / 537.36'}
response = requests.get(url, params=params, headers=headers)
print(response.url)