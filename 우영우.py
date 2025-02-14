inp = input('우 to the 영 to the 우')

똑바로 = []
거꾸로 = []
for i in range(len(inp)):
    똑바로.append(inp[i])
    거꾸로.append(똑바로.pop())

print(거꾸로, 똑바로)