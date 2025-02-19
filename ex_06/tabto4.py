import sys

# src = 'a.txt'
# dst = 'b.txt'

src = sys.argv[1]
dst = sys.argv[2]

try:
    f = open(src, 'r')
    tab_content = f.read()
    
except FileNotFoundError as e:
    print(f'{src}는 존재하지 않는 파일입니다')

finally:
    f.close()

tab_content = tab_content.replace('\t', '    ')

f = open(dst, 'w')
f.write(tab_content)

f.close()

print('\n완료되었습니다.\n')
