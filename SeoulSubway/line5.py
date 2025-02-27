import pandas as pd
file_path = './서울시지하철호선별역별승하차인원정보.csv'
data=pd.read_csv(file_path, encoding='EUC-KR')

# 열 이름 생성
columns = ['date','num','name','in','out','date2']
data.columns =columns
df = data.loc[:,:'out'] #out까지만 나오도록 설정

data = df.groupby(['num','name']).sum().reset_index()  #날짜별 승하차 합
data['total'] = data['in'] + data['out']       # 승하차 총합 생성
sdata = data[['num','name','total']]           # 승차,하차 제거
tdata = sdata[data['num'] == '5호선']          # 5호선만 나오도록 설정
tdata = tdata.sort_values(by=['total'], ascending=False) #오름차순 변경
total_data = tdata[['name','total']]           #이름과 총합만 나오도록 변경

#폰트 변경
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
d2_path = "./D2Coding-Ver1.3.2-20180524.ttf"
fm.fontManager.addfont(d2_path)
plt.rcParams['font.family'] = 'D2Coding'

# 상자 생성
import squarify
def square():
    plt.figure(figsize=(10,7))
    squarify.plot(sizes=total_data['total'],label=total_data['name'],alpha=0.3)  #alpha=밝기
    plt.rcParams['font.size']=8
    plt.rcParams['text.color']='blue'
    plt.gca().invert_yaxis()
    plt.axis('off')
    plt.show()

#그래프 생성
def graph():
    graph_data = total_data.iloc[:20]
    plt.figure(figsize=(40,30))
    plt.bar(x = graph_data['name'], height = graph_data['total'],color='blue')
    
    plt.xlabel('지하철역명', fontsize=50)
    plt.ylabel('승하차 인원(1=100만)', fontsize=50)
    plt.xticks(fontsize=15)  # x축 눈금 글씨 크기
    plt.yticks(fontsize=40)  # y축 눈금 글씨 크기
    plt.title('Seoul Line5', fontsize=60)
    plt.show()
