# Part 1
with open('input.txt', 'r') as inp:
    prev = None
    increases = 0
    for line in inp:
        value = line.strip()
        if not prev or prev < value:
            increases += 1
        prev = value

# print(increases)


# Part 2
with open('input.txt', 'r') as inp:
    lines = list(map(lambda i: int(i.strip()), inp))
    triples = zip(lines, lines[1:], lines[2:])
    sums = map(sum, triples)    
    prev = None
    increases = 0
    
    for value in list(sums):
        print(value)
        print(prev)
        
        if prev and prev < value:
            print('inc')
            increases += 1
        prev = value
        print('-')

print(increases)