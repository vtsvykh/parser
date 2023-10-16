#артикул, наименование, бренд, цена, скидка %, страна производитель
import requests

f = open('output.txt', 'w')
out = open('page.txt', 'w')
search = input().strip()
card_url = 'https://www.lamoda.ru/p/'
payload = {'q': search, 'sort': 'price_asc'}
#url = f'https://www.lamoda.ru/catalogsearch/result/?q={input().replace(" ","+")}&sort=price_asc'
url = 'https://www.lamoda.ru/catalogsearch/result'
#носки зеленые мужские adidas

response = requests.get(url, params=payload)
print(response)
page = response.text
idx = page.find('"products"')
new_page = page[idx:]
idxe = new_page.find('"products_meta"')
out.write(page[idx:idxe+idx])
# print(page[idx:idxe+idx])
len(page)
# print(page[page.find('"pagination"'):])
pagination = page.find('"pagination"')
pagitation_dict = page[pagination+13:pagination+page[pagination:].find('}')+1]
print(pagitation_dict)
f.write(pagitation_dict)
page_c = page

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
print(article_list, len(article_list))





'''
divs = a('x-product-card-description__microdata-wrap')
for div in divs:
	print(div.text_content())


print(url)
'''
# print(requests.get(url, params=payload).text)
# print(requests.get(url, params=payload).text)
# f.write(requests.get(url, params=payload).text)
#"x-product-card__card x-product-card__card_catalog"
#'x-product-card-description__microdata-wrap' цена
#'_value_ajirn_27 ui-product-description-attribute-production_country' страна
#артикул в ссылке
#"x-product-card-description__price-new x-product-card-description__price-WEB8507_price_no_bold _price_1okc5_8"

