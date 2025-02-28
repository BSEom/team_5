import requests as req
from bs4 import BeautifulSoup as bs

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'}
web = req.get(url, headers = headers)
soup = bs(web.content, 'html.parser')

title = soup.select('.ellipsis.rank01')
artist = soup.select('.service_list_song.type02 .ellipsis.rank02')

for i, (t, a) in enumerate(zip(title, artist),start=1):
    slices = int(len(a.text)/2)
    print(f"{i}위 : {t.text.strip()} / {a.text[:slices].strip()}")

if __name__ == '__main__':
    mel()