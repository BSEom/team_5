def stock_market():
    import requests as req
    from bs4 import BeautifulSoup as bs
    url = "https://finance.naver.com/sise/sise_market_sum.naver"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'}
    web = req.get(url, headers = headers)
    soup = bs(web.content,'html.parser')
    com = soup.select('.tltle')
    now = soup.select('td.number:nth-child(3)')
    for (c,n) in zip(com,now):
        print(f'{c.text} : {n.text}')

stock_market()