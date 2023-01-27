crds = [0, 0]
while (string := input()) != 'СТОП':
    num = int(input())
    match string:
        case 'СЕВЕР':
            crds[1] += num
        case 'ВОСТОК':
            crds[0] += num
        case 'ЮГ':
            crds[1] -= num
        case 'ЗАПАД':
            crds[0] -= num
print(crds[1], crds[0], sep='\n')
