import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import squarify

# 커스텀 폰트 로드 및 설정
d2_path = './D2Coding-Ver1.3.2-20180524.ttf'
fm.fontManager.addfont(d2_path)
plt.rcParams["font.family"] = "D2Coding"

# 데이터 로드
file_path = "./서울시지하철호선별역별승하차인원정보.csv"
raw = pd.read_csv(file_path, encoding='EUC-KR')

# 6호선 데이터 필터링
호선1 = raw[raw['호선명'] == '6호선']
호선1 = 호선1[['역명', '승차총승객수', '하차총승객수']]

# 역명별 그룹화 및 총 승객수 계산
역명그룹 = 호선1.groupby(['역명']).sum().reset_index()
역명그룹['총승객수'] = 역명그룹['승차총승객수'] + 역명그룹['하차총승객수']

def 총승객():
    """
    6호선 역별 총 승객수 상위 10개 역 시각화
    """
    # 총 승객수로 정렬하고 상위 10개 역 선택
    총승객 = 역명그룹.sort_values(by='총승객수', ascending=False)
    총승객10 = 총승객[:10]
    
    # 막대 그래프 생성
    plt.figure(figsize=(13, 6))
    plt.title('서울 지하철 6호선 총 승객별 Top 10')
    plt.bar(x=총승객10['역명'], height=총승객10['총승객수'] / 1000, color='orange')
    plt.xlabel('역명')
    plt.ylabel('총승객수 (천명)')
    plt.show()

def 승차승객():
    """
    6호선 역별 승차 승객수 상위 10개 역 시각화
    """
    # 승차 승객수로 정렬하고 상위 10개 역 선택
    승차 = 역명그룹.sort_values(by='승차총승객수', ascending=False)
    승차10 = 승차[:10]
    
    # 막대 그래프 생성
    plt.figure(figsize=(13, 6))
    plt.bar(x=승차10['역명'], height=승차10['승차총승객수'] / 1000, color='blue')
    plt.title('서울 지하철 6호선 승차 승객별 Top 10')
    plt.xlabel('역명')
    plt.ylabel('승차승객수 (천명)')
    plt.show()

def 하차승객():
    """
    6호선 역별 하차 승객수 상위 10개 역 시각화
    """
    # 하차 승객수로 정렬하고 상위 10개 역 선택
    하차 = 역명그룹.sort_values(by='하차총승객수', ascending=False)
    하차10 = 하차[:10]
    
    # 막대 그래프 생성
    plt.figure(figsize=(13, 6))
    plt.bar(x=하차10['역명'], height=하차10['하차총승객수'] / 1000, color='red')
    plt.title('서울 지하철 6호선 하차 승객별 Top 10')
    plt.xlabel('역명')
    plt.ylabel('하차승객수 (천명)')
    plt.show()

def 전체승객분포():
    """
    6호선 전체 역의 승객 분포 시각화
    """
    # 트리맵 생성
    plt.figure(figsize=(18, 8))
    squarify.plot(sizes=역명그룹['총승객수'], label=역명그룹['역명'])
    plt.rcParams["font.size"] = 12
    plt.rcParams["text.color"] = 'white'
    plt.gca().invert_yaxis()
    plt.axis("off")
    plt.show()
