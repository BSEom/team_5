from collections import Counter
from konlpy.tag import Komoran


def wcnt(sample_text):
    
    komoran = Komoran()
    sample_t = komoran.nouns(sample_text)
    sam_t = " ".join(sample_t)
    
    
    text_list = []
    count_t = {}
    count_list = []
    count_dic = {}

    
    temp_t = sam_t.split(' ')
    
    for i in temp_t:
        if i in text_list: continue
        text_list.append(i)
    
    for j in text_list:
        count_t[j] = temp_t.count(j)
    
    count_list = sorted(count_t.items(), key=lambda x:x[1], reverse=True) # 내림차순 정렬
    
    # print(count_list, type(count_list)) # 리스트 자료형
    
    for d in count_list:   # 딕셔너리 자료형 변환
        count_dic[d[0]] = d[1] 
    
    print(count_dic)

    print('\n')
    # 비교
    word_counts = Counter(sam_t.split())
    print(word_counts)

    # 워드클라우드
    wordcloud = WordCloud(font_path=font_path, width=800, height=400, background_color='white').generate(sam_t)
    
    # 시각화
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()
