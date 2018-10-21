import urllib.request
from webpage2 import scrapp 
import pandas as pd 
import datetime as dt
import csv 
import bs4 as bs
import requests as rq 
from webpage2 import scrapp


temp="C:/Users/Waqas/Desktop/Candev/TM_CIRNAC_02/webscrapper/"
links=[]
for a in range(1, 9):
	temp3 = "C:/Users/Waqas/Desktop/Candev/TM_CIRNAC_02/webscrapper/{}.html".format(a)
	#print(temp3)
	#temp3=str(a).append(".html")
	file1=temp3
	#file1="C:/Users/Waqas/Desktop/Candev/TM_CIRNAC_02/webscrapper/1.html"
	f= open(file1,"r+")
	#res=rq.get(file1)
	soup = bs.BeautifulSoup(f,"html.parser")

	mydivs=soup.find_all('div',class_='result result--news ')
	for div in mydivs:
		for temp in div.find_all('a',href=True):
			#print(temp['href'],"\n")
			links.append(temp['href'])		#(saving url to an array) End of secondary stories
			#print(temp['href']+"\t secondary")
			#break

	#print(soup.prettify())



with open("articlesFinal.csv",'w',newline='') as f:
	#thewriter=csv.writer(f)
	#thewriter.writerow(
	fieldnames=['date','title','author','url','article']
	thewriter=csv.DictWriter(f,fieldnames=fieldnames)
	thewriter.writeheader()

	temp2=set(links)
	#print(temp2,"\n")
	for b in temp2:
		topics_dict=scrapp(b)
		thewriter.writerow(topics_dict)



'''
file1="C:/Users/Waqas/Desktop/Candev/TM_CIRNAC_02/webscrapper/1.html"
f= open(file1,"r+")
#res=rq.get(file1)
soup = bs.BeautifulSoup(f,"html.parser")
print(soup.prettify())
'''