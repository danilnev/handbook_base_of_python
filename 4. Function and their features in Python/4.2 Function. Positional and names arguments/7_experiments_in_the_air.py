def enter_results(*args):
    global numbers
    numbers.extend(args)


def get_sum():
    global numbers
    sums = [0, 0]
    for i in range(len(numbers)):
        if i % 2 == 0:
            sums[0] += numbers[i]
        else:
            sums[1] += numbers[i]
    return round(sums[0], 2), round(sums[1], 2)


def get_average():
    global numbers
    nums1, nums2 = [], []
    for i in range(len(numbers)):
        if i % 2 == 0:
            nums1.append(numbers[i])
        else:
            nums2.append(numbers[i])
    return round(sum(nums1) / len(nums1), 2), round(sum(nums2) / len(nums2), 2)


numbers = []
enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())