from rtreelib import RTree, Rect, rtree, Point, RTreeGuttman
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
    query_set = o_query['data']
    return query_set


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


def query_processing(filename, r_tree):
    """
    Sequentially process the given query set.
    :param filename: task2.json
    :param r_tree: on static data
    """
    query_set = get_query(filename)

    for i in range(len(query_set)):

        res_dict = {}   # prepare for final result json.
        result = [] # poi_name list

        query_processing_time_s = time.time() * 1000

        nodes = r_tree.query_nodes(Rect(0, 0, 180, 180)) #  test
        # nodes = r_tree.query_nodes(Rect(query_set[i][0], query_set[i][1],
        #                         query_set[i][2], query_set[i][3]))
        # print(query_set[i][0], query_set[i][1],
        #                         query_set[i][2], query_set[i][3])

        query_processing_time_e = time.time() * 1000
        query_time = query_processing_time_e - query_processing_time_s

        res_dict['task_id'] = i + 1
        res_dict['query_time'] = query_time

        for j in nodes:
            for k in j.entries:
                print(oindex2poi.get(k.data).to_string())
                result.append(oindex2poi.get(k.data).to_string())

        res_dict['result'] = result

        with open("result/bundle0/range_query" + str(i + 1) + ".json", 'w', encoding='utf-8') as fp:
            json.dump(res_dict, fp)


if __name__ == "__main__":
    data_file = "data/bundle0/dataset.json"
    query_file = "data/bundle0/task2.json" # range query requirement.

    # Indexing only once.
    index_build_time_s = time.time()
    t = build_index(data_file)
    index_build_time_e = time.time()

    query_processing(query_file, t)


