a, b = int(input()), int(input())
all_sum = 0

for i in range(max(2, a), b + 1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        all_sum += i

print(all_sum)
