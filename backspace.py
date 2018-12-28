l = input()
output = ""
line = [char for char in l]
i = 1
while i < len(line):
    if line[i] == '<':
        line.pop(i)
        line.pop(i-1)
        i -= 1;
    else:
        i +=1
for x in line:
    output += x
if(len(line) > 0):
    print(output)
