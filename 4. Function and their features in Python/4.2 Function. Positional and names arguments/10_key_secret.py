import itertools


def secret_replace(text, **kwargs):
    string = text
    for key in kwargs:
        argument = kwargs[key]
        for arg in itertools.cycle(argument):
            string = string.replace(key, arg, 1)
            if key not in string:
                break
    return string


print(secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z")))
s = 'Hello, World!'
print(s.replace('l', 'hi'))
