import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

# Target URL
response = requests.get("https://vnexpress.net/the-thao")
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

# Target Title
titles = soup.findAll('h3', class_='title-news')
#print(titles, end='\n')
links = [link.find('a').attrs["href"] for link in titles]
#print(links)

class Insert (object):
    def __init__(self, title, abstract, body):
        self.title = title
        self.abstract = abstract
        self.body = body

last_j = []

for link in links:
 news = requests.get(link)
 #print(news)
 soup = BeautifulSoup(news.content, "html.parser")
 #print(soup)
 title = soup.find("h1", class_="title-detail")
 print("Tiêu đề: " +title.text)
 abstract = soup.find("p", class_="description")
 print("Mô tả: " +abstract.text)
 body = soup.find("p", class_="Normal")
 print("Nội dung: " +body.text)
 
 # Initialize to save data into JSON file
 insert = Insert(title.text,abstract.text,body.text)
 last_j.append(insert.__dict__)
 
 with open('data.json', 'w', encoding='utf-8') as file:
     json.dump(last_j, file)