import requests
from bs4 import BeautifulSoup as bs

url = "https://finance.naver.com/sise/sise_market_sum.naver"
req = requests.get(url)

def stock():
    soup = bs(req.content,'html.parser')
    title = soup.select("table.type_2 td a.tltle")
    price = soup.select("table.type_2 tr td:nth-child(3)")
    
    str = ''
    for t, p in zip(title, price):
        str += f"{t.text} : {p.text}원 \n"

    print(str)