import bs4 as bs 
import urllib.request
from webpage2 import scrapp 
import pandas as pd 
import datetime as dt
import csv 


links=[]
saurce= urllib.request.urlopen('https://www.cbc.ca/news/indigenous').read()
soup = bs.BeautifulSoup(saurce, 'lxml')

#print(soup.prettify())

#print(soup.title.text)

print(soup.p)

#print(soup.find_all('p'))
#print(soup.find_all('div'))

mydivs=soup.find_all('div',class_='secondaryTopStories')  #starting for secondary stories

#print("\n \n")
#print(mydivs,'\n')

#print(mydivs.find_all('href'))

for div in mydivs:
	#print(div.find_all('href'))
	for temp in div.find_all('a',href=True):
		#print(temp['href'],"\n")
		links.append("https://www.cbc.ca"+temp['href'])		#(saving url to an array) End of secondary stories
		print(temp['href']+"\t secondary")
		#print (links)

#print(links,len(links),"\n")


mydivs2=soup.find_all('div',class_='featuredTopStories')
for div in mydivs2:
	#print(div.find_all('href'))
	for temp in div.find_all('a',href=True):
		#print(temp['href'],"\n")
		links.append("https://www.cbc.ca"+temp['href'])
		print(temp['href']+"\t featuredTop")

mydivs3=soup.find_all('div',class_='featuredHighlights')
for div in mydivs3:
	#print(div.find_all('href'))
	for temp in div.find_all('a',href=True):
		#print(temp['href'],"\n")
		#print(temp,"		This is it")
		links.append("https://www.cbc.ca"+temp['href'])
		print(temp['href']+"\t featuredHighlights")

#print (links,len(links))

#topics_data = pd.DataFrame(columns=['date', 'title', 'author', 'url', 'article'])
topics_dict = { "date":[], \
	                "title":[], \
	                "author":[], \
	                "url":[], \
	                "article": []}
topics_data=pd.DataFrame(topics_dict)



with open("articles.csv",'w',newline='') as f:
	#thewriter=csv.writer(f)
	#thewriter.writerow(
	fieldnames=['date','title','author','url','article']
	thewriter=csv.DictWriter(f,fieldnames=fieldnames)
	thewriter.writeheader()




	for a in links:
		topics_dict=scrapp(a)
		#thewriter.writerow([topics_dict['date'],topics_dict["title"],topics_dict["author"],topics_dict["url"],topics_dict["article"]])
		#topics_data = pd.DataFrame(topics_dict)
		topics_dict["article"].replace('\u0313','')
		thewriter.writerow(topics_dict)

	#topics_data.to_csv('articles.csv', index=False)

#topics_data = pd.DataFrame(columns=['date', 'title', 'author', 'url', 'article')
#topics_data = pd.DataFrame(topics_dict)
#print(topics_data)

#for a in links:
#	print(a)

