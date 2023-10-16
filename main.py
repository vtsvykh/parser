"""
Case 2
Group:
Uchanov Igor
Fishchukova Sofia
Tsvykh Viktoria
"""

import requests

user_input = input('Введите Ваш запрос: ').replace(' ', '+')
url = 'https://www.lamoda.ru/catalogsearch/result/?q=' + user_input.replace(' ', '+')
print(url)

f = open('text.txt', 'w', encoding='utf_8')
r = requests.get(url)
text = r.text
f.write(text)
text = text.split('"')



# АРИТИКУЛ
# ЦЕНА
# СКИДКА
# НАИМЕНОВАНИЕ
# СТРАНА

# БРЭНД

page = 1
'''
for e in range(len(text)):
    if 'link' in text[e]:
        page = text[e + 2]
        print(page)
'''
url = 'https://www.lamoda.ru/catalogsearch/result/?q=' + user_input.replace(' ', '+') + '&page=' + str(page)
request = requests.get(url)
text = request.text
text = text.split('"')
with open('data.txt', 'w', encoding='utf_8') as data:
    while page < 5:  # найти количество страниц

        for element in range(len(text)):
            if 'x-product-card-description__brand-name' in text[element]:
                data.write(text[element + 1].strip("'</div><div class='") + '\n')  # ДОБАВЛЕНИЕ В ОБЩИЙ ФАЙЛ
        page += 1

        response = requests.get(url_product)

        names = get_name(page)
        for name in names:

            def get_name(page):
                name_list = []
                while True:
                    if page.find("name") != -1:
                        idx = page.find("name")
                        sign = page.find('",')
                        name = page[idx:sign].split(':')
                        name = name[8:]
                        if name != [''] and name[1][1:] not in name_list:
                            name_list.append(name[1][1:])
