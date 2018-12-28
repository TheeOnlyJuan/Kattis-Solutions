cases = int(input())

for _ in range(cases):
    input()
    total = 0
    kids = int(input())
    for x in range(kids):
        total += int(input())
    if(total % kids == 0):
        print('YES')
    else:
        print('NO')
        
