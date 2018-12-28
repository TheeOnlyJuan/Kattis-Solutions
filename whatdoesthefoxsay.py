for i in range(int(input())):
    words = input().split()
    sounds = set()
    output = ""
    while True:
        line = input()
        if len(line.split()) == 3:
            sounds.add(line.split()[2])
        else:
            for x in words:
                if x not in sounds:
                    output += x + " "
            break
    print(output.strip())
