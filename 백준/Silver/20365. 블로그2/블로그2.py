n = int(input())
rb = input()

b = 0
r = 0

prev = ''
for color in rb:
    if prev != color:
        if color == 'B':
            r += 1
        else:
            b += 1
    prev = color

print(min(r,b) + 1)