d = dict()
ops = ['+','-','*','//']

for x in range(4):
    for y in range(4):
        for z in range(4):
            equation = '4 ' + ops[x] + ' 4 ' + ops[y]+ ' 4 ' + ops[z] + ' 4'
            d[eval(equation)] = equation
    
for i in range(int(input())):
    num = int(input())
    if num in d:
        print(d[num].replace("//", "/"),"=",num)
    else:
        print('no solution')
