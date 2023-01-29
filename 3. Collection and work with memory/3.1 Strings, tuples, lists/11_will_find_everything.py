num = int(input())
titles = []
for i in range(num):
    titles.append(input())
search_word = input()
for title in titles:
    if search_word.lower() in title.lower():
        print(title)
