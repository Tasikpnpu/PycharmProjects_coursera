a = int(input())
b = int(input())
n = int(input())

D = (((a * 100 + b) * n) // 100)
C = (((a * 100 + b) * n) % 100)
print(D, C)
