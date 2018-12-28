while True:
    try:
        # your code here
        i = input()
        i = i.split(" ")
        num1 = int(i[0])
        num2 = int(i[1])
        print(abs(num1-num2))
    except :
        break
