import math


num1, num2 = map(int, input().split())
print(math.comb(num1, num2) * num2 // num1, math.comb(num1, num2))
