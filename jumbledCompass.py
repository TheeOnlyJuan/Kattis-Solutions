start = int(input())
stop = int(input())
offset = (360-start + stop) % 360
if (offset > 180):
    print(offset-360)
else:
    print(offset)
