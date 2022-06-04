import json

datafile = "data/bundle0/dataset.json"

with open(datafile, encoding='utf-8') as f:
    all_data = json.load(f)

indexs = all_data['index']

# index 的 value 是什么意思？

pois = all_data['data']

# print(indexs)
# print(pois)



for i in range(len(pois)):
    if pois[i][1] > 31.26669374323893 and pois[i][2] > 121.53663879013597 and pois[i][1] < 32.277351826123098 and  pois[i][2] < 121.54823912361209:
        print(pois[i])




