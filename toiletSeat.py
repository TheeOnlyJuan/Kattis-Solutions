positions = input()
start = positions[0]

p1 = 0
if(positions.startswith('UD')):
    p1 = 2
elif(positions.startswith('DD') or positions.startswith('DU')):
    p1 = 1
p1 += positions[2:len(positions)].count('D') * 2
    
p2 = 0
if(positions.startswith('DU')):
    p2 = 2
elif(positions.startswith('UU') or positions.startswith('UD')):
    p2 = 1
p2 += positions[2:len(positions)].count('U') * 2

p3 = 0
for i in range(len(positions)-1):
    if(positions[i] != positions[i+1]):
        p3 += 1
print(p1,p2,p3,sep = '\n')
