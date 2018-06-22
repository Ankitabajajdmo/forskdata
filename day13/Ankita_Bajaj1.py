from urllib.request import urlopen
url="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
page= urlopen(url)

from bs4 import BeautifulSoup
soup=BeautifulSoup(page,"lxml")

right_table=soup.find("table",class_= "wikitable")

state=[]
national_share=[]

count=0
for row in right_table.findAll("tr"): 
    if count>6:
        break
    cells=row.findAll("td")
    if len(cells) == 7:    
        state.append(cells[1].text.strip())
        national_share.append(cells[4].text.strip())
    count+=1
    
import matplotlib.pyplot as plt

labels = state
sizes =national_share
explode=[0]*len(sizes)
explode[0] = 0.1  # only "explode" the 1st slice 

plt.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)
 
plt.axis('equal')
plt.show()
