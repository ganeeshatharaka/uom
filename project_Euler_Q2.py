a = 1
b = 2
even_sum = 2
limit = 4000000

while True:
    c = a + b

    if c > limit:
        break

    if c % 2 == 0:
        even_sum += c

    a = b
    b = c

print(even_sum)