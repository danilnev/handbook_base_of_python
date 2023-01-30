import sys

heights_above = []
heights_before = []
lines = sys.stdin.readlines()
for line in lines:
    line = line.rstrip('\n')
    heights_above.append(int(line.split()[1]))
    heights_before.append(int(line.split()[2]))
middle_h_above = sum(heights_above) / len(heights_above)
middle_h_before = sum(heights_before) / len(heights_before)
print(round(middle_h_before - middle_h_above))
