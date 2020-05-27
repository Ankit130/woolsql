import openpyxl
import os
import requests
from bs4 import BeautifulSoup as soup


def reset():
    url='https://www.woolworths.com.au/sitemap1.xml'
    r=requests.get(url)
    Soup=soup(r.text,'html.parser')
    urls=Soup.findAll('loc')
    links=[]
    for url in urls[:5000]:
        if('productdetails' in url.text and 'donation' not in url.text):
            link=url.text
            key=link.split('/')[5]
            ur='https://www.woolworths.com.au/apis/ui/product/'+str(key)+'/Stores?IncludeInStockStoreOnly=false&Max=500&Postcode=2000'
            #ur='https://www.woolworths.com.au/apis/ui/product/detail/'+str(key)+'?isMobile=false'
            #print(ur)
            links.append([ur,key])
    with open('data.txt','w') as f:
        for link in links:
            f.write(link[0]+'|'+link[1]+'\n')

    with open('cache.txt','w') as f:
        for i in range(1,35):
            f.write(str(i)+'|No\n')



def geturl():
    with open('cache.txt','r') as f:
        data=f.readlines()
        for d in data:
            flag=d.split('|')[1]
            if('No' in flag):
                #key=d.split('|')[1]
                return d.split('|')[0]
    return None

def update():
    with open('cache.txt','r') as f:
        data=f.readlines()
    with open('cache.txt','w+') as f:
        fg=1
        for d in data:
            flag=d.split('|')[1]
            if('No' in flag and fg==1):
                flag='yes\n'
                fg=0
            f.write(d.split('|')[0]+'|'+flag)
        

def getdata():
    with open('data.txt','r') as f:
        data=f.readlines()
        return data
