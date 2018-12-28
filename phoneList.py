cases = int(input())
contacts = []
for i in range(cases):
    valid = True
    contacts.clear()
    conSize = int(input())
    for x in range(conSize):
        contacts.append(input())
    for x in range(conSize-1):
        for y in range(x+1,conSize):
            if(contacts[y].startswith(contacts[x])):
                x = conSize
                y = conSize
                valid = False
    if(valid):
        print("YES")
    else:
        print("NO")
