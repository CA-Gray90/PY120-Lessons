import json

with open('TO_ascii_title.json', 'r') as file:
    title = json.load(file)

for line in title['title']:
    print(line)