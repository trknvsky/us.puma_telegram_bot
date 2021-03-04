import requests
from bs4 import BeautifulSoup
from decimal import Decimal


def get_html(url, cgid, from_price, to_price):
    params = {
        'cgid': cgid,
        'start': 0,
        'sz': 2000,
        'isAjax': 1
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
               'AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 39.0.2171.95Safari / 537.36'}
    response = requests.get(url, params=params, headers=headers)
    contents = response.text
    soup = BeautifulSoup(contents, 'lxml')
    items_data = []
    products = soup.find_all('div', {'class': 'product-tile'})
    count = 0
    for product in products:
        item = {}
        d_none = product.find_all('div', {'class': 'd-none'})
        tile_body = product.find_all('div', {'class': 'product-tile-info-container'})
        # print(tile_body)
        product_images = product.find_all('div', {'class': 'product-tile-image-container image-container'})
        for item_names in d_none:
            names = item_names.find_all('span', {'itemprop': 'name'})
            for name in names:
                item['name'] = name.contents[0]
        for product_image in product_images:
            product_tile_images = product_image.find_all('a', {'class': 'product-tile-image-link tile-image-link'})
            for product_tile_image in product_tile_images:
                product_tile_pictures = product_tile_image.find_all('picture', {'class': 'tile-picture js-picture-lazy'})
                for product_tile_picture in product_tile_pictures:
                    images = product_tile_picture.find_all('img', {
                        'class': 'product-tile-image product-tile-image--default tile-image'})
                    img = images[0].get('data-src').replace('450', '2000').replace("’", "").replace("bv", "mod01")
                    chars_counter = 1
                    while chars_counter != 8:
                        img = img.replace(f"sv0{chars_counter}", 'sv01').replace(f"dt0{chars_counter}", "sv01")
                        chars_counter += 1
                    item['img'] = img
        for values in tile_body:
            hrefs = values.find_all('a', {'class': 'product-tile-link product-tile-title pdp-link line-item-limited'})
            prices = values.find_all('div', {'class': 'product-tile-info-price'})
            for href in hrefs:
                item['href'] = 'https://us.puma.com{}'.format(href.get('href'))
            for price in prices:
                item['price'] = price.contents[1].contents[0][1:]
                item['currency'] = 'USD'
                if len(price.contents[1].contents[0][1:]) > 3:
                    item_price = Decimal(price.contents[1].contents[0][1:])
                    if item_price != '':
                        if item_price > Decimal(from_price) and item_price < Decimal(to_price):
                            count += 1
                            item['count'] = count
                            items_data.append(item)

    return items_data
