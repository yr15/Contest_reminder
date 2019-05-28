import urllib.request
from bs4 import BeautifulSoup
import datetime

url="https://codechef.com/contests"

req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

html = urllib.request.urlopen(req)






soup=BeautifulSoup(html,'lxml')



title = soup.title
print('title')

containers=soup.findAll("tr")
containers=containers[0:20]

now = datetime.datetime.now()

y=int(now.strftime("%Y"))
m=int(now.strftime("%m"))
d=int(now.strftime("%d"))

Dict={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

for container in containers:        
    name=container.findAll("td")	
    if(len(name)>3):	
       l=name[2].text.strip()
       
       lis=l[0:11].split()
       #print(lis)
       
       if    len(lis)!=3 or  Dict.get(lis[1] ,0)==0:
           continue
       lis_m=int(Dict[lis[1]])
       lis_d=int(lis[0])
       lis_y=int(lis[2])
       
       
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
	   	               
        
   
       
        
	   
