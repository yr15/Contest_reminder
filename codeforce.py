#from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import datetime

url="https://codeforces.com/contests"

html=urlopen(url)

soup=BeautifulSoup(html, 'lxml')


title = soup.title

containers=soup.findAll("tr")


now = datetime.datetime.now()

y=int(now.strftime("%Y"))
m=int(now.strftime("%m"))
d=int(now.strftime("%d"))

Dict={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

for container in containers:
	
        
	name=container.findAll("td")
	
	
	if(len(name)>0):
	   
	   l=name[2].text.strip()
	   lis=l[0:11].split('/')
	   lis_m=Dict[lis[0]]  #month
	   lis_d=int(lis[1])   #day
	   lis_y=int(lis[2])   #year
	   
	   if(lis_y>=y ):
	   	  if(lis_y>y):
	   	     print(name[0].text.strip())
	   	  else:
	   	     if(lis_m>=m):
	   	        if(lis_m>m):
	   	          print(name[0].text.strip())
	   	        else:
	   	        	if(lis_d>=d):
	   	        		print(name[0].text.strip())