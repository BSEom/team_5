from collections import Counter
from konlpy.tag import Komoran

sample_text = """
햇살이 밝게 빛나는 아침, 저는 행복한 마음으로 공원을 산책했습니다. 공원에서는 많은 사람들이 행복하게 웃고 있었고, 행복한 아이들이 뛰어놀고 있었습니다. 행복한 기운이 가득한 이곳에서, 모든 사람들은 행복한 시간을 보내고 있었습니다. 행복한 날씨와 행복한 사람들 덕분에, 저도 더욱 행복해졌습니다. 이 행복한 순간을 오래도록 기억하고 싶습니다. 행복, 행복, 그리고 또 행복.
"""

komoran = Komoran()
sample_t = komoran.nouns(sample_text)
sam_t = " ".join(sample_t)


text_list = []

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

# 비교
word_counts = Counter(sam_t.split())
print(word_counts)