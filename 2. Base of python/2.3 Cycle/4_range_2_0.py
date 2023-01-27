begin = int(input())
end = int(input())
if begin > end:
    print(*range(begin, end - 1, -1))
else:
    print(*range(begin, end + 1))
