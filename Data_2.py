import requests
import pickle
import bs4 

res=requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
soup=bs4.BeautifulSoup(res.text,"lxml")
table=soup.find('table',{'class':'wikitable sortable'})
print(table)
tickles=[]
new=""
for i in table.findAll("tr")[1:]:
    tickle=i.findAll("td")[0].text 
    for i in tickle:
        if i!="\n":
            new+=i
        else:
            tickles.append(new)
            new=""
            break
print(tickles)
with open('sp500_tickers.pickle','wb') as f:
    pickle.dump(tickles,f)

