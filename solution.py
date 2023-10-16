"""
Case 2
Group:
Uchanov Igor       80%
Fishchukova Sofia  45%
Tsvykh Viktoria    50%
"""

import requests
import json
from requests import Response

f = open('output.txt', 'a', encoding='utf_8')
search = input().strip()
card_url = 'https://www.lamoda.ru/p/'
payload = {'q': search, 'sort': 'price_asc', 'page': 1}
url = 'https://www.lamoda.ru/catalogsearch/result'

response = requests.get(url, params=payload)
page = response.text
idx = page.find('"products"')
new_page = page[idx:]
idxe = new_page.find('"products_meta"')

pagination = page.find('"pagination"')
pagitation_dict = page[pagination + 13:pagination + page[pagination:].find('}') + 1]

num_pages = json.loads(pagitation_dict)['pages']


def get_artikules(page):
    article_list = []
    while True:
        if page.find("short_sku") != -1:
            idx = page.find("short_sku")
            sign = page.find('",')
            article = page[idx:sign].split(':')
            page = page[26:]
            if article != [''] and article[1][1:] not in article_list:
                article_list.append(article[1][1:])
        else:
            break
    return article_list


def get_name(page):
    if page.find('x-premium-product-title-new__model-name"') != -1:
        idx = page.find('x-premium-product-title-new__model-name"')
        end = page[idx:].find('</div>')
        name = page[idx:idx + end]
        return name[41:]
    elif page.find('"x-premium-product-title__model-name"') != -1:
        idx = page.find('"x-premium-product-title__model-name"')
        end = page[idx:].find('</div>')
        return page[idx + 38:idx + end]


def get_dicount(page):
    if page.find('"discount_lamoda_amount"') != -1:
        idx = page.find('"discount_lamoda_amount"')
        discount = page[idx - 10:idx]
        start = discount.find(':')
        end = discount.find(',')
        return discount[start + 1:end]
    else:
        return 0


def get_brand(page):
    if page.find('"Бренд"') != -1:
        idx = page.find('"Бренд"')
        end = page[idx:].find('/",')
        brand = page[idx: idx + end]
    return brand[brand.find("-") + 1:]


def get_country(page):
    idx = page.find('"Страна производства"')
    if idx != -1:
        country = page[idx:idx + 100]
        start = country.find('"value"')
        country = country[start:]
        country = country[9:]
        end = country.find('"')
        return country[:end]


def get_price(page):
    idx = page.find('"priceCurrency"')
    if idx != -1:
        price = page[idx:idx + 50]
        start = price.find('"price": "')
        end = price.find('.')
        price = price[start + 10:end]
        return price


def get_product_info(page, artikul):
    return (f'{artikul} {get_name(page_product)} {get_brand(page_product)} {get_country(page_product)} '
            f'{get_price(page_product)} {get_dicount(page_product)}\n')


for page in range(1, num_pages + 1):
    payload['page'] = page
    response = requests.get(url, params=payload)
    page = response.text
    artikules = get_artikules(page)
    for artikul in artikules:
        url_product = f'https://www.lamoda.ru/p/{artikul}'
        page_product = requests.get(url_product).text
        product = get_product_info(page_product, artikul)
        f.write(product)
