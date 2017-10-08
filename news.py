from bs4 import BeautifulSoup
import requests
import re

search_phrase = "asdfalsidhfalsdhfalsdkhfljhaeef wow"
page = requests.get("https://news.google.com/news/search/section/q/" + search_phrase)

soup = BeautifulSoup(page.content, "lxml")

i = 26
for a in soup.find_all('a')[26:35]:
	print("Link #" + str(i) + "\n")
	print(str(a) + "\n")
	i += 1

href = soup.find_all('a')[26].get('href')
# TODO If href is redirected to google.com, end the program
print(href)