import json
import os
os.system("cls")

data=[
    {"id":1, "name":"sayyid", "age": 20},
    {"id":2, "name":"ahmed", "age": 30},
    {"id":3, "name": "ali", "age": 40}
]

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4 , ensure_ascii=False)

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)

for r in data:
    r["aktif"]=True

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)