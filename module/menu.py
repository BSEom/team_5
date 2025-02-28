import requests
from bs4 import BeautifulSoup as bs

url = "https://www.pusan.ac.kr/kor/CMS/MenuMgr/menuListOnBuilding.do?mCode=MN202"
req = requests.get(url)
soup = bs(req.content,'html5lib')
table = soup.select(".menu-tbl")
menu = soup.select(".menu-tbl tbody tr td > ul > li p")
day = soup.select(".menu-tbl .day")
date = soup.select(".menu-tbl .date")

for date, day, menu in zip(date, day, menu):
    print(date.text, day.text)
    print(menu.text.strip() + '\n')