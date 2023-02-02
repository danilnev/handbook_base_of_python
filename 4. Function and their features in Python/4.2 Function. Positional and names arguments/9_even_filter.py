print(*filter(lambda num: sum([int(x) for x in str(num)]) % 2 == 0, (32, 64, 128, 256, 512)))
