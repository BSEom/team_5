import datetime

def pday():
    days = ['월', '화', '수', '목', '금', '토', '일']
        
    p_day = datetime.date(2025,5,8)
    today = datetime.datetime.now().date()

    diff3 = p_day - today

    print("어버이날까지 " + str(diff3.days) + "일 남았습니다. 어버이날은 " + days[p_day.weekday()] + "요일 입니다.")
