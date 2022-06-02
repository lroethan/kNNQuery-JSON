from dataclasses import dataclass
from typing import List
import json
from rtree import index
import config_0


def get_data(filename: str):
    with open(filename, encoding='utf-8') as f:
        all_data = json.load(f)
    indexs = all_data['index']
    pois = all_data['data']
    return indexs, pois

def get_bound(data: list):
    lat_lst, lon_lst = [], []
    # lat->x, lon->y
    for item in data:
        lat_lst.append(item[1])
        lon_lst.append(item[2])
    xmin, xmax = min(lat_lst), max(lat_lst)
    ymin, ymax = min(lon_lst), max(lon_lst)
    return [xmin, xmax, ymin, ymax]


def get_config(filename: str, configname: str):
    ids, pois = get_data(filename)
    bound_pos = get_bound(pois)
    bound = ['xmin','xmax','ymin','ymax']
    with open(configname, 'a+') as f:
        f.write("index_cnt={}\n".format(len(ids)))
        f.write("poi_cnt={}\n".format(len(pois)))
        for i in range(4):
            f.write("{}={}\n".format(bound[i], bound_pos[i]))


@dataclass
class POI():
    id: int
    pos: tuple

class MyRtree(object):
    def __init__(self, pois: List[POI]) -> None:
        self.idx = index.Index()
        for p in pois:
            self.idx.insert(p.id, p.pos, obj=p)
        

         

if __name__ == "__main__":
    ids, pois = get_data("data/bundle0/dataset.json")
    my_rtree = []
    delta = 1e-11
    for i in range(config_0.index_cnt):
        id_i = ids[i]
        pos_i = (pois[i][1]-delta, pois[i][2]-delta, pois[i][1]+delta, pois[i][2]+delta)
        my_rtree.append(POI(id=id_i, pos=pos_i))
    my_rtree = MyRtree(my_rtree)
    # my_rtree中此时已经对所有poi以MBR的形式建立好相关索引
    
    # get_config("data/bundle0/dataset.json", 'config_0.py')
    # get_config("data/bundle1/dataset.json", 'config_1.py')
    