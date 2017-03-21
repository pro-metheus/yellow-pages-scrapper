#scrap bot
import requests
from bs4 import BeautifulSoup as bs
headers={'user-agent':'robot 1.0'}
url='http://www.yellowpageskerala.in/'
m=input('what ?:')
n=input('where?:')
if n is ' ':
    n='for'
    
#payload={'what':m,'where':n,'siteroot':'http://www.yellowpageskerala.in/'}
url='http://www.yellowpageskerala.in/search/'+str(n)+'/'+str(m)
r=requests.get(url)
soup=bs(r.text,'html.parser')
content=soup.find_all('div', class_='content')
print(content)
for c in content:
    print(c.text)
