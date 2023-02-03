import requests
from bs4 import BeautifulSoup
from decimal import Decimal


def get_html(url, from_price, to_price):
    response = requests.get(url)
    contents = response.text
    soup = BeautifulSoup(contents, 'lxml')

    items_data = []
    count = 0

    products = soup.find_all('li', {'data-test-id': 'product-list-item'})

    for product in products:
        item = {}

        item['name'] = product.find('h3').text
        item['url'] = 'https://us.puma.com' + product.find('a', {'data-test-id': 'product-list-item-link'}).get('href')
        item['img'] = product.find('img').get('src').replace('300', '2000').replace('”-', "-").replace('"-', '-')

        price = product.find('span', {'data-test-id': 'sale-price'})
        if not price:
            price = product.find('span', {'data-test-id': 'price'})
        item['price'] = price.text

        item_price = Decimal(item['price'].split('$')[-1])
        if item_price != '':
            if Decimal(from_price) < item_price < Decimal(to_price):
                count += 1
                item['count'] = count
                items_data.append(item)

    return items_data
