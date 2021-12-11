import json
with open('menu.json') as json_file:
    data = json.load(json_file)
print(data)
'''có 2 cách hiển thị dữ liệu'''
print(data['menu'])
print(data.get('menu'))