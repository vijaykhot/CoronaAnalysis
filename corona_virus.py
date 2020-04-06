# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:20:50 2020

@author: Vijay Khot
"""
#                corona virus Analysis
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


url='https://www.worldometers.info/coronavirus/'


#request to the website worldometers
r=requests.get(url)
#print(r)

#parsing html file to beutifulsoup
html=r.text
soup=BeautifulSoup(html,'html.parser')

#Extract Basic Data
print(soup.title.text)
print()
live_data=soup.find_all('div',id='maincounter-wrap')
#print(live_data)
for i in live_data:
    print(i.text)
    

print("Analysis based on individual Countries")

#Extracting table data
table_body=soup.find('tbody')
table_rows=table_body.find_all('tr')

countries=[]
cases=[]
todays=[]
deaths=[]
recovered=[]

for tr in table_rows:
    td = tr.find_all('td')
    countries.append(td[0].text)
    cases.append(td[1].text)
    todays.append(td[2].text)
    deaths.append(td[3].text)
    recovered.append(td[5].text)
    
#print(recovered)    
indices=[i for i in range(1,len(countries)+1)]    
headers=['Countries/othr','Total Cases','Todays Cases','Deaths','Recovered']  
df=pd.DataFrame(list(zip(countries,cases,todays,deaths,recovered)),columns=headers,index=indices)
df.to_csv('corona-analysisww.csv')
print(df)  

#ploting the bar graph
y_pos=[i for i in range(1,len(countries)+1)]
plt.bar(y_pos,cases[::-1],align='center',alpha=0.1)
plt.xticks(y_pos,countries,rotation=90)
plt.ylabel('Total Cases')
plt.title('Persons affected by corona virus')
plt.savefig('corona-analysisww.png',dpi=600)
plt.show()    
    

