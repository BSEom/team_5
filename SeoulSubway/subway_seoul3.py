def line3():
    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm
    import squarify
    
    file_path = "./ref/서울시지하철호선별역별승하차인원정보.csv"
    df = pd.read_csv(file_path,encoding="EUC-KR")
    df['total'] = df['승차총승객수'] + df['하차총승객수']
    total_data = df[['호선명','역명','total']]
    data = total_data[total_data['호선명']=='3호선']
    gdata = data.groupby(by='역명').sum().reset_index()
    tdata = gdata[['역명','total']]
    sdata = tdata.sort_values(by='total',ascending=False)
    
    d2_path = "./ref/D2Coding-Ver1.3.2-20180524.ttf"
    fm.fontManager.addfont(d2_path)
    plt.rcParams["font.family"] = "D2Coding"
    
    plt.figure(figsize=(25,7))
    squarify.plot(sizes=sdata['total'], label = [f"{x[0]}({x[1]}명)" for x in zip(sdata['역명'],sdata['total'])],alpha=0.5)
    plt.rcParams['font.size'] = 10
    plt.gca().invert_yaxis()
    plt.axis("off")
    plt.show()