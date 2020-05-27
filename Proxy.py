import asyncio
from proxybroker import Broker
import sys
import os
import random 
import requests
from selenium import webdriver

Proxies=[]
async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None:
            break
        print('Found proxy: %s' % proxy)
        Proxies.append(proxy)


def saveproxy():
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(
        broker.find(types=['HTTP', 'HTTPS'], limit=20 ), show(proxies)
    )
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
    import time
    print(Proxies)
    with open('proxies.txt','w') as f:
        for proxy in Proxies:
                proxy=str(proxy)
                proxy=proxy[proxy.rfind(']')+2:proxy.find('>')]
                f.write(proxy+'|'+'Yes\n')

async def saveproxy1():                    
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(
        broker.find(types=['HTTP', 'HTTPS'], limit=20 ), show(proxies)
    )
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
    import time
    print(Proxies)
    with open('proxies.txt','w') as f:
        for proxy in Proxies:
                proxy=str(proxy)
                proxy=proxy[proxy.rfind(']')+2:proxy.find('>')]
                f.write(proxy+'|'+'Yes\n')
def proxylist():
    proxies=[]
    with open('proxies.txt','r') as f:
        proxy=f.readlines()
    for pro in proxy:
        if('Yes' in pro.split('|')[1]):
            proxies.append(pro.split('|')[0])
    return proxies

def getrandomproxy():
    proxies=proxylist()
    if(len(proxies)<10):
        try:
            saveproxy1()
        except:
            pass
        return getrandomproxy()
    return random.choice(proxies)

def markproxy(proxy):
    with open('proxies.txt','r') as f:
        data=f.readlines()
    
    with open('proxies.txt','w') as f:
        for d in data:
            if(proxy in d):
                f.write(d.replace('Yes','No'))
            else:
                f.write(d)

def my_proxy(PROXY):
        webdriver.DesiredCapabilities.FIREFOX['proxy']={
            "httpProxy":PROXY,
            "ftpProxy":PROXY,
            "sslProxy":PROXY,
            
            "proxyType":"MANUAL",
            
        }
        return webdriver.Firefox()   
    

