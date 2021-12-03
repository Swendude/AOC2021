# part 1
with open('input.txt', 'r') as inp:
    n_lines = 1
    summed = None
    for line in inp:
        n_lines += 1
        int_line = list(map(int, line.strip()))
        if not summed:
            summed = int_line
        else:
            for i in range(len(summed)):
                summed[i] += int_line[i]
gamma = [0 for _ in range(len(summed))]
epsilon = [0 for _ in range(len(summed))]
for i in range(len(summed)):
    if summed[i] >= (n_lines/2):
        gamma[i] = 1
        epsilon[i] = 0
    else:
        gamma[i] = 0
        epsilon[i] = 1
print(gamma)
g_int = int((''.join(map(str,gamma))),2)
e_int = int((''.join(map(str,epsilon))),2)
print(g_int * e_int)
# print(epsilon)
# print(summed)
# print(n_lines)

# print(h_pos, d, h_pos * d)