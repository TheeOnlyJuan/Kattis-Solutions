n = int(input())
prices = [0] * n
for x in range(n):
    prices[x] = int(input())
prices.sort(reverse=True)
total = 0
for i in range(0,n,3):
    if (n - i > 2):
        total += sum(prices[i:i+3])- min(prices[i:i+3])
    else:
        total += sum(prices[i:n])
       
print(total)
