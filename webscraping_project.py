from bs4 import BeautifulSoup
import requests
import csv
for page in range(6):
	labtops_titles=[]
	labtops_prices=[]
	url=requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=labtop&_sacat=0&_pgn={number}')
	soup=BeautifulSoup(url.content,'html.parser')
	titles=soup.findAll(attrs={'class':'s-item__title'})
	prices=soup.findAll(attrs={'class':'s-item__price'})
	for title in titles:
		labtops_titles.append(title.text)
	for price in prices:
                labtops_prices.append(price.text)
labtops=pd.DataFrame({"labtops_titles":labtop_titles,'labtops_prices':labtops_prices})
for page in range(6):
        phones_titles=[]
        phones_prices=[]
        url=requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=phone&_sacat=0&_pgn={number}')
        soup=BeautifulSoup(url.content,'html.parser')
        titles=soup.findAll(attrs={'class':'s-item__title'})
        prices=soup.findAll(attrs={'class':'s-item__price'})
        for title in titles:
                phones_titles.append(title.text)
        for price in prices: 
                phones_prices.append(price.text)
phones=pd.DataFrame({"phones_titles":phones_titles,'phones_prices':phones_prices})
for page in range(6):
        smart_watches_titles=[]
        smart_watches_prices=[]
        url=requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=smart+watch&_sacat=0&_pgn={number}')
        soup=BeautifulSoup(url.content,'html.parser')
        titles=soup.findAll(attrs={'class':'s-item__title'})
        prices=soup.findAll(attrs={'class':'s-item__price'})
        for title in titles:
                smart_watches_titles.append(title.text)
        for price in prices: 
                smart_watches_prices.append(price.text)
smart_Watches=pd.DataFrame({"smart_watches_titles":smart_watches_titles,'smart_watches_prices':smart_watches_prices})
for page in range(6):
        consoles_titles=[]
        consoles_prices=[]
        url=requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=game+console&_sacat=0&_pgn={number}')
        soup=BeautifulSoup(url.content,'html.parser')
        titles=soup.findAll(attrs={'class':'s-item__title'})        
        prices=soup.findAll(attrs={'class':'s-item__price'})
        for title in titles:
                consoles_titles.append(title.text)
        for price in prices:  
                consoles_prices.append(price.text)
consoles=pd.DataFrame({"consoles_titles":consoles_titles,'consoles_prices':consoles_prices})
for page in range(6):
        earbuds_titles=[]
        earbuds_prices=[]
        url=requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=Earbuds&_sacat=0&_pgn={number}')
        soup=BeautifulSoup(url.content,'html.parser')
        titles=soup.findAll(attrs={'class':'s-item__title'})        
        prices=soup.findAll(attrs={'class':'s-item__price'})
        for title in titles:
                earbuds_titles.append(title.text)
        for price in prices:  
                earbuds_prices.append(price.text)
earbuds=pd.DataFrame({"earbuds_titles":earbuds_titles,'earbuds_prices':earbuds_prices})
