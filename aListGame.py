import math
def biggestfactor(x):
    for i in range(2, int(math.sqrt(x))+1):
       if x % i == 0:
           return(x//i)
    return x
num = int(input())
bf = 0
count = 0
while(True):
    bf = biggestfactor(num)
    count +=  1
    if(bf == num):
        break
    num = bf
print(count)
