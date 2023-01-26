num1 = input()
num2 = input()
summ = ''
while len(num1) > len(num2):
    num2 = '0' + num2
while len(num2) > len(num1):
    num1 = '0' + num1
for i in range(len(num1)):
    summ += str(int(num1[i]) + int(num2[i]))[-1]
print(summ)
