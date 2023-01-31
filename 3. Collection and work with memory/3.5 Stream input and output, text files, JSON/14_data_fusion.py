import json
import sys

first_json = input()
second_json = input()
data = dict()
with open(file=first_json, encoding='utf-8') as users_file:
    users = json.load(users_file)
for user in users:
    name = user['name']
    data[name] = dict()
    for key in user:
        if key != 'name':
            data[name][key] = user[key]
with open(file=second_json, encoding='utf-8') as updates_file:
    updates = json.load(updates_file)
for i in range(len(updates)):
    update = updates[i]
    name = update['name']
    for key in update.keys():
        if key != 'name':
            if key in data[name]:
                data[name][key] = max([updates[i][key], data[name][key]])
            else:
                data[name][key] = updates[i][key]
with open(file=first_json, mode='w', encoding='utf-8') as output_json:
    json.dump(data, output_json, ensure_ascii=False, indent=4)
