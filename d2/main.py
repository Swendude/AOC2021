# part 1
with open('input.txt', 'r') as inp:
    commands = []
    h_pos = 0
    d = 0
    for line in inp:
        command, amount = line.strip().split(' ')
        if command == 'forward':
            h_pos += int(amount)
        if command == 'down':
            d += int(amount)
        if command == 'up':
            d -= int(amount)

# print(h_pos, d, h_pos * d)

# part 2
with open('input.txt', 'r') as inp:
    commands = []
    h_pos = 0
    d = 0
    aim = 0
    for line in inp:
        command, amount = line.strip().split(' ')
        if command == 'forward':
            h_pos += int(amount)
            d += int(aim) * int(amount)
        if command == 'down':
            aim += int(amount)
        if command == 'up':
            aim -= int(amount)

print(h_pos, d, h_pos * d)

