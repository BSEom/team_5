import datetime

def birthday():
    inp = input("주민번호 앞자리 입력 ㄱㄱ")
    while len(inp) != 6:
        print("큰일났음 다시 입력해주삼")
        inp = input("주민번호 앞자리 입력 ㄱㄱ")  
    
    month = inp[2:4]
    if month[0] == "0":
        month[0].replace("0","")
    date = inp[4:]
    if date[0] == "0":
        date[0].replace("0","")
    birthday = datetime.date(2025,int(month),int(date))
    today = datetime.datetime.now().date()
        
    birthday_diff = today - birthday
    days = ['월','화','수','목','금','토','일']
    birthday_days = birthday.weekday()
        
    if birthday_diff.days < 0:
        print(f"생일 {days[birthday_days]}요일이네 {abs(birthday_diff.days)}일 남았다 미리 ㅊㅊㅊㅊ")
    elif birthday_diff.days > 0:
        print(f"생일 {days[birthday_days]}요일이었네 {abs(birthday_diff.days)}일 지났네")
    else:
        print("오늘 생일임? ㅊㅊㅊㅊ")