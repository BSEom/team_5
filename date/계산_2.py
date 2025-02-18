import datetime

def childrens():
    chil = datetime.date(2025,5,5)
    today = datetime.datetime.now().date()
    week = ['월','화','수','목', '금' , '토', '일']
    day = chil - today
    print("어린이날은",week[chil.weekday()]+"요일입니다. 현재 어린이날까지",day.days,"일 남았습니다.")