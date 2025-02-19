def write():
    f = open("memo.txt",'a',encoding = "utf-8")
    while 1:
        inp = input("메모를 작성하시오(멈추기:stop):")
        if inp == 'stop':
            break
        f.write(inp+'\n')
    f.close

def read():
    f = open("memo.txt",'r',encoding = 'utf-8')
    while 1:
        line = f.readline()
        if not line: 
            break
        print(line)
    f.close