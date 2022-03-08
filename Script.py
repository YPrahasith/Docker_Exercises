import sys
from bs4 import BeautifulSoup
import requests

headlines = []
file_path = 'abc.txt'
url = 'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
links=soup.find_all('a',attrs={'class':'DY5T1d RZIKme'})
for j in links:
    if j not in headlines:
            headlines.append(j.text+"\n")
        
with open(file_path,"w") as o:
    o.writelines(headlines)