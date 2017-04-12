from bs4 import BeautifulSoup
import urllib3
import re
import os
import webbrowser

url = input("Anna artikkelin osoite: ")
conn = urllib3.PoolManager()
pageconn = conn.request('GET', url)
pagedata = pageconn.data
soup = BeautifulSoup(pagedata, 'html.parser')

div_id = "ArticleBody"
regexd = re.compile('%s-\d*'%div_id)

article = soup.find("div", id=regexd)
headline = soup.find('h1', attrs = {'class' : 'article-title'})
author = soup.find('a', attrs = {'itemprop' : 'author'})

file = open("hesaripage.html", "w+")
file.write("<html><head><meta charset=\"UTF-8\"></head>")
file.write(headline.prettify())
if author:
	file.write(author.prettify())
file.write(article.prettify())
file.write("</html>")
file.close()

webbrowser.open_new_tab('file://' + os.path.dirname(os.path.abspath(__file__)) + "/hesaripage.html")

print("HTML-tiedosto valmis, avataan..")

