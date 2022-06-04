from rtreelib import RTree, Rect, rtree, Point
import priority_queue
import json
import config_0
import time
import sys

from Poi import Poi

# K-V dict which maintained in memory, to obtain the final name or useful information.
oindex2poi = {}


def get_query(filename: str):
    """
    Read query JSON and return the query rectangle.
    :param filename: task2.json
    :return: querys: list
    """
    with open(filename, encoding='utf-8') as f:
        o_query = json.load(f)
    querys = o_query['data']
    return querys


def build_index(filename: str):
    """
    Build indexes on static datasets
    :param filename: dataset.json
    :return t: R-Tree on dataset.json
    """

    # 1. Data source
    with open(filename, encoding='utf-8') as f:
        o_data = json.load(f)
    o_index = o_data['index']
    o_poi = o_data['data']

    # 2. Transform data. example: '107' : '107, 苏州大学, 30, 120'. The dict is global.
    for i in range(len(o_index)):
        oindex2poi[o_index[i]] = Poi(o_index[i],
                                     o_poi[i][0], o_poi[i][1], o_poi[i][2])

    # 3. Build R-tree by sequentially inserting KEY and Rect.
    t = RTree()
    for i in oindex2poi.keys():
        t.insert(i, Rect(oindex2poi[i].get_lat(), oindex2poi[i].get_lon(),
                         oindex2poi[i].get_lat(), oindex2poi[i].get_lon()))

    # 4. Return R-tree. The R-tree is used for all search processing, i.e, one fits all.
    return t


def query_processing(filename, t):
    querys = get_query(filename)
    for i in range(len(querys)):
        pass



if __name__ == "__main__":
    data_file = "data/bundle0/dataset.json"
    query_file = "data/bundle0/task1.json"
    result_file = "result/bundle0/result1.json"

    index_build_time_s = time.time()
    t = build_index(data_file)
    index_build_time_e = time.time()



    query_processing_time_s = time.time()

    # for i in entries:
    #     print(i.data)

    # nodes = t.query_nodes(Rect(user_query[0], user_query[1], user_query[2], user_query[3]))
    nodes = t.query_nodes(Rect(30.0, 120.0, 32.0, 122.0))
    for i in nodes:
        for j in i.entries:
            print(oindex2poi.get(j.data).get_name())
    # entries = t.query(Rect(0,0,180,180))

    query_processing_time_e = time.time()
