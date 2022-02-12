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
        product_images = product.find_all('div', {'class': 'product-tile-image-container image-container'})
        # NAMES
        for item_names in d_none:
            names = item_names.find_all('span', {'itemprop': 'name'})
            for name in names:
                item['name'] = name.contents[0]
        # IMAGES
        for product_image in product_images:
            carousel_slides = product_image.find_all('div', {'class': 'glide-carousel-slides'})
            for carousel_slide in carousel_slides:
                slides = carousel_slide.div
                pictures = slides.find_all('picture', {'class': 'tile-picture js-picture-lazy'})
                for picture in pictures:
                    image_urls = picture.find_all('img', {'class': 'product-tile-image product-tile-image--default tile-image'})
                    for image_url in image_urls:
                        image = image_url.get('data-src')
                item['img'] = image.replace("’", "").replace("w_450", "w_2000").replace("h_450", "h_2000")
        # URLS AND PRICES
        for values in tile_body:
            print(values)
            hrefs = values.find_all('a', {'class': 'product-tile-title product-tile__title pdp-link line-item-limited line-item-limited--2'})
            prices = values.find_all('div', {'class': 'product-tile-info-price'})
            for href in hrefs:
                item['href'] = 'https://us.puma.com{}'.format(href.get('href'))
            for price in prices:
                item['price'] = price.contents[1].contents[0][1:]
                item['currency'] = 'USD'
                if len(price.contents[1].contents[0][1:]) > 3:
                    item_price = Decimal(price.contents[1].contents[0][1:])
                    if item_price != '':
                        if Decimal(from_price) < item_price < Decimal(to_price):
                            count += 1
                            item['count'] = count
                            items_data.append(item)
    return items_data
