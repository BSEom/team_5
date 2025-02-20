import requests as req
from bs4 import BeautifulSoup as bs
def stock():
    url = 'https://finance.naver.com/sise/sise_market_sum.naver'
    
    web = req.get(url)
    soup = bs(web.content, 'html.parser')
    title = soup.select('.tltle')
    price = soup.select( '.no+td+td')
    total = soup.select( '#contentarea > div.box_type_l > table.type_2 > tbody > tr > td:nth-child(7)') 
    
    
    
    for i, (t,p,tt) in enumerate(zip(title,price,total),1):
        print(f'no.{i}:{t.text}\n현재가: {p.text} /시가총액: {tt.text}')
