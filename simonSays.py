output = ""
for i in range(int(input())):
    line = input()
    if(i == 0):
       first = line 
    if line.startswith("simon says") and line != first or i == 0:
        output += line[11:] + "\n"
    else:
        output += "\n"
print(output.strip())
