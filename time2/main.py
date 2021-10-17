n = int(input())

s = str(n % 60 // 10) + str(n % 60 % 10)
m = str(n // 60 % 60 // 10) + str(n // 60 % 10)
h = str(n // 60 // 60 % 24)

print(h, m, s, sep=':')
