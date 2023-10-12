"""
Case 2
Group:
Uchanov Igor
Fishchukova Sofia
Tsvykh Viktoria
"""

import requests

user_input = input('Введите Ваш запрос: ')
url = 'https://www.lamoda.ru/catalogsearch/result/?q=' + user_input
r = requests.get(url)
text = r.text

