string = 'мама мыла раму'
print(sorted(string.split(), key=lambda text: (len(text), text.lower())))
string = 'Яндекс использует Python во многих проектах'
print(sorted(string.split(), key=lambda text: (len(text), text.lower())))

