data = [
    {"id": 123, "name": "Kevin"},
    {"id": 234, "name": "Bob"}
]

temp = {}

for i in data:
    temp[i.get("id")] = {"name": i.get("name")}

print temp