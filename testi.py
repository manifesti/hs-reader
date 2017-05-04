from bs4 import BeautifulSoup, Tag
import urllib3
import re
import os
import webbrowser

# get user input, load imports and download the article
#!/usr/bin/python3

url = input("Anna artikkelin osoite: ")
conn = urllib3.PoolManager()
pageconn = conn.request('GET', url)
pagedata = pageconn.data
soup = BeautifulSoup(pagedata, 'html.parser')

# id of the content div is ArticleBody and a random number sequence
div_id = "ArticleBody"
regexd = re.compile('%s-\d*'%div_id)

# find the content divs
article = soup.find("div", id=regexd)
headline = soup.find('h1', attrs = {'class' : 'article-title'})
author = soup.find('a', attrs = {'itemprop' : 'author'})

# load images from article
for tag in article.find_all('figure'):
	if tag is not None:
		image = tag.find('img')
		image['src'] = "http:" + image['src']
		tag.replaceWith(image)

# write the HTML-file
file = open("hesaripage.html", "w+")
file.write("<html><head><meta charset=\"UTF-8\"><title>hs.fi reader</title><link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css\" integrity=\"sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u\" crossorigin=\"anonymous\"></head>")
file.write("<body><div class=\"container\"><div class=\"page-header\">")
file.write(headline.prettify())
file.write("</div>")
if author:
	file.write(author.prettify())
file.write(article.prettify())
file.write("</div></html>")
file.close()

#open the file in browser
webbrowser.open_new_tab('file://' + os.path.dirname(os.path.abspath(__file__)) + "/hesaripage.html")
print("HTML-tiedosto valmis, avataan..")

