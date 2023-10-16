#артикул, наименование, бренд, цена, скидка %, страна производитель
import requests
import json
from requests import Response
f = open('output.txt', 'w')
out = open('page.txt', 'w')
search = input().strip()
card_url = 'https://www.lamoda.ru/p/'
payload = {'q': search, 'sort': 'price_asc', 'page': 1} 
#url = f'https://www.lamoda.ru/catalogsearch/result/?q={input().replace(" ","+")}&sort=price_asc'
url = 'https://www.lamoda.ru/catalogsearch/result'

#классный запрос, всего 7 товаров, легко отлаживать
#носки зеленые мужские adidas

response = requests.get(url, params=payload)
print(type(response))
page = response.text
idx = page.find('"products"')
new_page = page[idx:]
idxe = new_page.find('"products_meta"')
# out.write(page[idx:idxe+idx])

# print(page[idx:idxe+idx])
len(page)
# print(page[page.find('"pagination"'):])
pagination = page.find('"pagination"')
pagitation_dict = page[pagination+13:pagination+page[pagination:].find('}')+1]
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


for page in range(num_pages):
	response = requests.get(url, params=payload)
	page = response.text
	arlikules = get_artikules(page)
	for arlikul in arlikules:
		url_product = f'https://www.lamoda.ru/p/{arlikul}'
		print(url_product)
		page_product = requests.get(url).text
		#out.write(page_product)
		#TODO: сюда добалять код чтобы доставать наименование, бренд, цена, скидка %, страна производитель
ur = 'https://www.lamoda.ru/p/RTLACV944401'
page_product = requests.get(ur).text
out.write(page_product)
