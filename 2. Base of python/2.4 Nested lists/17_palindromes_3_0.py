palindrome_count = 0
for i in range(int(input())):
    number = ''.join(input().split())
    if number == ''.join(reversed(list(number))):
        palindrome_count += 1
print(palindrome_count)
