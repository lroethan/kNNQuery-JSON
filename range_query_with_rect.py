from rtreelib import RTree, Rect, rtree
import priority_queue
import json
import config_0
import time

from Poi import Poi


def build_index(filename: str):
    """
    对静态数据集构建索引
    :param filename: 文件路径
    :return t: R-Tree
    """

    # 读取数据集
    with open(filename, encoding='utf-8') as f:
        o_data = json.load(f)
    o_index = o_data['index']
    o_poi = o_data['data']

    # 构建 KV 字典
    oindex2poi = {}  # key 为 o_index（数据集里的 index），value 为 Poi 实例，暂定为三/四元组。
    for i in range(len(o_index)):
        oindex2poi[o_index[i]] = Poi(o_index[i],
                                     o_poi[i][0], o_poi[i][1], o_poi[i][2])

    # 构建 R-Tree
    t = RTree()
    for i in oindex2poi.keys():
        t.insert(i, Rect(oindex2poi[i].get_lat(), oindex2poi[i].get_lon(),
                         oindex2poi[i].get_lat(), oindex2poi[i].get_lon()))

    return t


if __name__ == "__main__":
    data_file = "data/bundle0/dataset.json"
    query_file = "data/bundle0/task1.json"
    result_file = "result/bundle0/result1.json"

    t = build_index(data_file)

    entries = t.query(Rect(config_0.xmin, config_0.ymin, config_0.xmax, config_0.ymax))

    print(entries)