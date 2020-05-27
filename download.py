from function import *
from Proxy import *
import os
from bs4 import BeautifulSoup as soup
import csv
import requests
import time
from itertools import islice





flag=True
def scrape(urls,g):
  rows=[]
  for i,url in enumerate(urls):
    url=url.split('|')
    print(i,url[0],g)
    try:
        r=requests.get(url[0],timeout=30)
        data=r.json()
    except:
        return rows,False
    for d in data:
      row=[url[1],1]
      row.append(d['Store']['StoreNo'])
      for a in d:
        if(a=='Store'):
          continue
        row.append(d[a])
      rows.append(row)
  return rows,True  


def download():
    k=geturl()
    print(k)
    if(k==None):
        return None
    data=getdata()
    k=int(k)
    try:
        data=data[(k-1)*1000:k*1000]
    except:
        update()
        return k
    print(k,len(data))
    rows,flag=scrape(data,k)
    if(flag==False):
        time.sleep(1000)
        return k
    
    import openpyxl
    wb=openpyxl.Workbook()
    sht=wb.active
    for row in rows:
                sht.append(r)
    wb.save('Output'+str(k)+'.xlsx')
    update()
    return k
        
#reset()

    
