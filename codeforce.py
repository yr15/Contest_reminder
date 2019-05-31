from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import datetime
import sqlite3
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


conn = sqlite3.connect('db.sqlite3') #data base se connect karne ke liye
i=0
i=int(i)

cursor = conn.execute("SELECT id, name, DATETIM from CONTEST")  # database ke items cursor me store karne ke liye


for container in containers:

	name=container.findAll("td")
	if(len(name)>0):
		l=name[2].text.strip()
		lis=l[0:11].split('/')
		lis_m=Dict[lis[0]]  #month
		lis_d=int(lis[1])   #day
		lis_y=int(lis[2])   #year
		n=str(name[0].text.strip())
		lis=str(lis)
		x=0
        
		if(lis_y>=y ):
			if(lis_y>y):
				#x=0
				for rows in cursor:
					if(n==rows[1]):
						x=1
				if(x==0):
					i=i+1 # line 54 se 57 tak data ko database me bharne ke liye
					para=(i,n,lis)
					conn.execute("INSERT INTO CONTEST (ID,NAME,DATETIM) \
						VALUES (?,?,?)",para);
					conn.commit()
			else:
				if(lis_m>=m):
					if(lis_m>m):
						#x=0
						for rows in cursor:
							if(n==rows[1]):
								x=1
								print(x)
						if(x==0):
							i=i+1
							para=(i,n,lis)
							conn.execute("INSERT INTO CONTEST (ID,NAME,DATETIM) \
								VALUES (?,?,?)",para);
							conn.commit()
					else:
						if(lis_d>=d):
							#x=0
							for rows in cursor:
								if(n==rows[1]):
									x=1
									print(x)
							if(x==0):
								i=i+1
								para=(i,n,lis)
								conn.execute("INSERT INTO CONTEST (ID,NAME,DATETIM) \
									VALUES (?,?,?)",para);
								conn.commit()


