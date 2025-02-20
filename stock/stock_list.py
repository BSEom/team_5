import requests as req
from bs4 import BeautifulSoup as bs


# ebs

def stock_list():
    url = 'https://finance.naver.com/sise/lastsearch2.naver'
    web = req.get(url)
    soup = bs(web.content, 'html.parser')

    no = soup.select('.type_5 td.no')
    price = soup.select('.type_5 td:nth-child(4)')
    name = soup.select('.type_5 td a')

    
    
    for num, n, p in zip(no, name, price):
        print(num.text, n.text + ':', p.text + '원')