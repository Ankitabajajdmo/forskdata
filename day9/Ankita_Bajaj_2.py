from urllib.request import urlopen

wiki="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

page= urlopen(wiki)

from bs4 import BeautifulSoup

soup=BeautifulSoup(page,"lxml")

#all_tables=soup.find_all("table")

right_table=soup.find("table",class_="table")

a=[]
b=[]
c=[]
d=[]
e=[]

for row in right_table.findAll("tr"):
    cells=row.findAll("td")
    if len(cells)==5:
        a.append(cells[0].find(text=True))
        b.append(cells[1].text.strip())
        c.append(cells[2].find(text=True))
        d.append(cells[3].find(text=True))
        e.append(cells[4].find(text=True))
        
import pandas as pd
df=pd.DataFrame(a,columns=["Pos"])
df["Team"]=b
df["Matches"]=c
df["Points"]=d
df["Rating"]=e
print(df)