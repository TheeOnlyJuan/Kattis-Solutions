line = input().split()
h = int(line[0])
path = ""
if len(line)> 1:
    path = line[1]
node = 2**(int(h)+1)-1
level = 1
for char in path:
    if char == 'L':
        node -= level
        level *= 2
    else:
        node -= level + 1
        level = level*2 + 1

print(node)
