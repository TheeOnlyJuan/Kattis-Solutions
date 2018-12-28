for n in range(int(input())):
    winner = 0
    total = 0
    highest = 0
    for i in range(int(input())):
        votes = int(input())
        total += votes
        if(highest < votes):
            highest = votes
            winner = i + 1
        elif(highest == votes):
            winner = 0
    if (winner == 0):
        print('no winner')
    elif(highest > total/2):
        print('majority winner', winner)
    else:
        print('minority winner', winner)
