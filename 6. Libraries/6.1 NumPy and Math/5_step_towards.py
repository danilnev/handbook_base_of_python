import math


crds1 = tuple(map(float, input().split()))
p, f = map(float, input().split())
crds2 = p * math.cos(f), p * math.sin(f)
print(math.dist(crds1, crds2))
