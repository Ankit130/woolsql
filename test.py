import requests
from bs4 import BeautifulSoup as soup

headers={
    'Host': 'www.handwerker-radar.de',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-GB,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Referer': 'https://www.handwerker-radar.de/5100,111,hwrlist.html',
'Cookie': 'JSESSIONID=y85WZKVMGrge9OXoTVAfw5uJfxogLc9mcc-JmCUUCQvhOV3gGxNI!366127550; ROUTEID=.node1; odav-cookie-consent={"consents":{"technical":true,"analytics":true,"extmedia":true},"uuid":"b77a5e1a-4ad2-4fe5-90eb-31e456d0f8d7","version":1}',
'Upgrade-Insecure-Requests': '1'}

r=requests.get('https://www.handwerker-radar.de/5100,111,hwrlist.html?hwrsearchpage=2&plz=52062&radius=250',headers=headers)
Soup=soup(r.text,'html.parser')

#print(Soup)
divs=Soup.findAll('div',attrs={'class':'hwrdetail hidden'})
print(divs[0])

