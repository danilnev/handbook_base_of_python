hours = int(input())
minutes = int(input())
delivery = int(input())
hours = (hours + ((minutes + delivery) // 60)) % 24
minutes = (minutes + delivery) % 60
if hours < 10:
    hours = '0' + str(hours)
else:
    hours = str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
else:
    minutes = str(minutes)
print(hours + ':' + minutes)
