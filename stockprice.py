#Scrapes Yahoo finance for stock price of choice
import pandas as pd
import requests
from bs4 import BeautifulSoup

ticker = input("ticker symbol? ").lower()
res = requests.get("https://finance.yahoo.com/quote/"+ticker)
soup = BeautifulSoup(res.content,'lxml')

price = soup.find_all("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})[0]
print(price.text)