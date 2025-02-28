import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import json
import os

load_dotenv()
KEY = os.getenv("KEY")

today_date = datetime.today().strftime("%Y-%m-%d").replace("-","") #오늘 날짜
yesterday_date = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d").replace("-","") #어제 날짜 (영화 순위 업데이트가 안돼서 어제 날짜로 해야 잘 나옴)

url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={KEY}&targetDt={yesterday_date}&itemPerPage=10&repNationCd=K"
req = requests.get(url)
data = req.json()['boxOfficeResult']['dailyBoxOfficeList']

print(f"========== {today_date} 영화 순위 ==========")
for i in range(10):
    print(f"{i + 1}위 : {data[i]['movieNm']}")