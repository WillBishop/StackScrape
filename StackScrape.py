import requests
from bs4 import BeautifulSoup
import urllib
import sys
import os

page = 0
try:
	if not os.path.exists("Saved"):
		os.makedirs("Saved")
	urllib.request.urlretrieve("https://cdn.sstatic.net/Sites/stackoverflow/all.css?v=267c70aa775e", "Saved/all.css") #Yeah yeah, I know, not effective, it's a couple KB
except Exception as e: #Empty except, pls don't kill me
	print(e)
	pass
tag = sys.argv[1]
while True:
	page += 1
	r = requests.get("http://stackoverflow.com/questions/tagged/%s?page=%d" % (tag, page))
	soup = BeautifulSoup(r.text, 'html.parser')
	links = {}
	for i in soup.findAll('a', {'class': 'question-hyperlink'}, href=True):
		if 'questions' in i['href']:
			links[i.getText()] = "http://stackoverflow.com" + i['href'] 
	for i in links:
		name = "".join([c for c in i if c.isalpha() or c.isdigit() or c==' ']).rstrip()

		try:
			with open("Saved/%s.html" % name, 'wb') as f:
				content = requests.get(links[i]).text.replace("https://cdn.sstatic.net/Sites/stackoverflow/all.css?v=267c70aa775e", "all.css")
				f.write(content.encode('utf-8'))
		except:
			pass
