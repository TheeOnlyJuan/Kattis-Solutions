import sys
input()
nums = input()
counts = [0]*6
for i in range(1,7):
    counts[i-1] = nums.count(str(i))
for i in range(5,-1,-1):
    if(counts[i] == 1):
        print(nums.find(str(i+1))//2 + 1)
        sys.exit()
print('none')
