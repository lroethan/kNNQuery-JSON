import json

datafile = "data/bundle0/dataset.json"

with open(datafile, encoding='utf-8') as f:
    all_data = json.load(f)

indexs = all_data['index']

# index 的 value 是什么意思？

pois = all_data['data']

# print(indexs)
print(pois)

