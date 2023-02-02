def is_palindrome(obj):
    if type(obj) in [int, float]:
        obj = str(obj)
    obj = list(obj)
    reversed_obj = list(reversed(obj))
    if obj == reversed_obj:
        return True
    else:
        return False


print(is_palindrome(1221))
