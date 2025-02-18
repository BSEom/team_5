import datetime

def xmas():
    today = datetime.datetime.now().date()
    xmas = datetime.date(2025,12,25)
    dday = xmas - today
    print("크리스마스까지", f'{dday.days}' + '일 남았습니다.')

    days = ['월','화','수','목','금','토','일']
    print("크리스마스는", f"{days[xmas.weekday()]}"+"요일 입니다.")