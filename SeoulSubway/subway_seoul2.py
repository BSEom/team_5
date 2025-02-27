import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import squarify


def subway_line2():  
    
    file_path = "./서울시지하철호선별역별승하차인원정보.csv"
    data = pd.read_csv(file_path, encoding="EUC-KR")
    
    col = ['date', 'line', 'stage', 'type_1', 'type_2', 'update']
    data.columns = col
    
    
    df = data.loc[:, :'type_2']     # 갱신일 제거
    
    df['total'] = df['type_1'] + df['type_2']  # 승,하차 통합, 컬럼 추가
    
    df = df[['date', 'line', 'stage', 'total']] # 승,하차 컬럼 제거
    
    gdata = df.sort_values(by=['date', 'line'], ascending=[True, True])  # 호선, 날짜로 정렬
    
    test = gdata.groupby(by=['line','stage']).sum().reset_index() # 역별로 전체 이용객 통합
    
    tdata = test[['line', 'stage', 'total']] # 날짜 제거
    
    fdata = tdata[tdata['line'] == '2호선'] # 2호선 추출
    
    # fdata.sort_values(by='total', ascending=False) # 이용객순 정렬

    matp(fdata)
    

def matp(data):

    d2_path = "./D2Coding-Ver1.3.2-20180524.ttf"
    
    fm.fontManager.addfont(d2_path)
    plt.rcParams["font.family"] = "D2Coding"
    
    plt.figure(figsize=(15,10))
    plt.rcParams['font.size'] = 10
    plt.rcParams['text.color'] = "black"
    squarify.plot(sizes=data['total'], label=data.stage, alpha=0.7)
    # squarify.plot(sizes=data['total'].iloc[:20], label=data['stage'].iloc[:20], alpha=0.7)
    
    plt.gca().invert_yaxis() # 축 뒤집기
    plt.axis("off") # 축 인덱스 없애기
    plt.show()

    