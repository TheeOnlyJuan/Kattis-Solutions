d = dict()
output = ""
try:
    
    while(True):
        temp = input()
        if(temp == ""):
            break
        d[temp.split()[1]] = temp.split()[0]
    while(True):
        temp = input()
        if temp in d:
            output += d[temp] + '\n'
        else:
            output += 'eh\n'
except: 
    print(output)
