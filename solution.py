# артикул, наименование, бренд, цена, скидка %, страна производитель
import requests
import json
from requests import Response

f = open('output.txt', 'w')
out = open('page.txt', 'w')
search = input().strip()
card_url = 'https://www.lamoda.ru/p/'
payload = {'q': search, 'sort': 'price_asc', 'page': 1}
# url = f'https://www.lamoda.ru/catalogsearch/result/?q={input().replace(" ","+")}&sort=price_asc'
url = 'https://www.lamoda.ru/catalogsearch/result'
# носки зеленые мужские adidas

response = requests.get(url, params=payload)
print(type(response))
page = response.text
idx = page.find('"products"')
new_page = page[idx:]
idxe = new_page.find('"products_meta"')
out.write(page[idx:idxe + idx])

# print(page[idx:idxe+idx])
len(page)
# print(page[page.find('"pagination"'):])
pagination = page.find('"pagination"')
pagitation_dict = page[pagination + 13:pagination + page[pagination:].find('}') + 1]
print(pagitation_dict)
f.write(pagitation_dict)
page_c = page

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
    name_list = []
    while True:
        if page.find("name") != -1:
            idx = page.find("name")
            sign = page.find('",')
            name = page[idx:sign].split(':')
            name = name[1]
            if name != [''] and name[1][1:] not in name_list:
                name_list.append(name[1][1:])
        else:
            break
    return name_list



for page in range(num_pages):
    payload['page'] = page
    response = requests.get(url, params=payload)
    page = response.text
    arlikules = get_artikules(page)

    for arlikul in arlikules:
        url_product = f'https://www.lamoda.ru/p/{arlikul}'
        names = get_name(page)
        print(names)
        