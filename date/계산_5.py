import datetime

def chuseok():

    days = ['월', '화', '수', '목', '금', '토', '일']
    
    fin_date = datetime.date(2025,7,25)
    chuseok_date = datetime.date(2025,10,6)
    
    result = chuseok_date - fin_date

    print(f'{fin_date} 수료 후 추석까지 {result.days}일 남고, 추석 당일은 {days[chuseok_date.weekday()]}요일 입니다.')