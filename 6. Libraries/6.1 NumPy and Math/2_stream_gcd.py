import math
import sys


data = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
print('\n'.join(map(lambda x: str(math.gcd(*x)), data)))
