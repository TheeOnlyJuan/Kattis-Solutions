input()
trees = input()
days = [int(s) for s in trees.split()]
days = sorted(days, reverse=True)
count = len(days)
left = [days[i]-count+i for i in range(count)]
print(max(left)+ count+2)

