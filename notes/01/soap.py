from time import sleep

import requests
from bs4 import BeautifulSoup

#
# page_url = 'https://en.wikipedia.org/wiki/Oggy_and_the_Cockroaches'
# response = requests.get(page_url)
# soup = BeautifulSoup(response.content, 'html.parser')
#
# img_el = soup.find(alt='Oggy and the Cockroaches tittle.jpg')
# img_url = 'https:' + img_el.get('src')
# img = requests.get(img_url, allow_redirects=True)
#
# open('oggy_cat.jpg', 'wb').write(img.content)


# ------------ 2

# url = "http://vkurse.dp.ua/"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# cur = soup.find(id='euroBuy')
# print(cur)


# --------------- 3

url = 'https://doroshenkoaa.ru/med/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
article_list = soup.find_all("a", {"class": "more"})
for art in article_list:
	page_url = art.get('href')
	article_page = requests.get(page_url)
	soup_page = BeautifulSoup(article_page.content, 'html.parser')
	article_body = soup_page.find("div", {"itemprop": "articleBody"})
	print(article_body)

