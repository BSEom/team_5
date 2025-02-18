import datetime

def birthday():
    
    inp = input("생일 언제임 (월, 일만 입력해주고 숫자가 한자리이면 앞에 0붙여주기 안그러면 큰일남 귀찮게 해서 ㅈㅅ)")
    inp = inp.replace('월','').replace('일','').replace('-','').replace(' ', '')
    
    if len(inp) != 4:
        print("큰일났음 다시 입력해주삼")
        inp = input("생일 언제임 (월, 일만 입력해주고 숫자가 한자리이면 앞에 0붙여주기 안그러면 큰일남 귀찮게 해서 ㅈㅅ)")
    else:
        month = int(inp[:2].replace('0', ''))
        date = int(inp[2:].replace('0', ''))
        birthday = datetime.date(2025,month,date)
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