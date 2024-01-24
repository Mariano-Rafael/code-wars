in_cont = 0
out_cont = 0

n = int(input())

for i in range(n):
    x = int(input())

    if 10 <= x <= 20:
        in_cont += 1
    else:
        out_cont += 1

print(f'{in_cont} in\n', f'{out_cont} out')





