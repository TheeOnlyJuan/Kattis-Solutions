import sys
b = []
for i in range(8):
    b.append([c for c in input()])
    count = b[i].count("*")
    if(count != 1):
        print("invalid")
        sys.exit()
for row in range(8):
    for col in range(8):
        if(b[row][col] == '*'):
            #checks above
            r = row -1
            while r >= 0:
                if(b[r][col] == '*'):
                    print("invalid")
                    sys.exit()
                else:
                    r -= 1
            #checks below
            r = row +1
            while r < 8:
                if(b[r][col] == '*'):
                    print("invalid")
                    sys.exit()
                else:
                    r += 1
            #checks up left
            r = row -1
            c = col -1
            while(c >= 0 and r >= 0):
                if(b[r][c] == '*'):
                    print("invalid")
                    sys.exit()
                else:
                    r -= 1
                    c -= 1
            #checks up right
            r = row -1
            c = col +1
            while(c < 8 and r >= 0):
                if(b[r][c] == '*'):
                    print("invalid")
                    sys.exit()
                else:
                    r -= 1
                    c += 1
            #checks down right
            r = row +1
            c = col +1
            while(c < 8 and r < 8):
                if(b[r][c] == '*'):
                    print("invalid")
                    sys.exit()
                else:
                    r += 1
                    c += 1
            #checks down left
            r = row +1
            c = col -1
            while(c >= 0 and r < 8):
                if(b[r][c] == '*'):
                    print("invalid")
                    sys.exit()
                else:
                    r += 1
                    c -= 1
print('valid')
