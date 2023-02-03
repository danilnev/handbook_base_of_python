def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
        if j < len(right):
            result.extend(right[j:])
        elif i < len(left):
            result.extend(left[i:])
        return result


print(merge_sort([3, 1, 5, 3, 15, 2, 54, 98, 3, 9]))
