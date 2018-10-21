import bs4 as bs 
import urllib.request
import pandas as pd 
import datetime as dt

def scrapp(url):
	saurce= urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(saurce, 'lxml')
	topics_dict = { "date":[], \
	                "title":[], \
	                "author":[], \
	                "url":[], \
	                "article": []}

	topics_dict["url"].append(url)

	author=soup.find_all('span',class_='authorText')
	for a in author:
		topics_dict["author"].append(a.text)

	time=soup.find_all('time',class_='timeStamp')
	for a in time:
		topics_dict["date"].append(a['datetime'])

	title=soup.find_all('title')
	for a in title:
		topics_dict["title"].append(a.text.replace(" | CBC News",""))



	ba= "a"
	paragraphs=soup.find_all('p')
	for a in paragraphs:

		ba=ba+a.text
		ba.replace("\u0313"," ")
	topics_dict["article"].append(ba)
	return topics_dict 