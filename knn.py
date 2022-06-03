from rtreelib import RTree, Rect, rtree
import priority_queue
import json
import config_0
visit_cnt = 0
import time


'''
获取 POI
'''
def get_data(filename: str):
    with open(filename, encoding='utf-8') as f:
        all_data = json.load(f)
    indexs = all_data['index']
    pois = all_data['data']
    return indexs, pois


'''
获取 Query
'''
def get_query(filename: str):
    with open(filename, encoding='utf-8') as f:
        all_data = json.load(f)
    querys = all_data['data']
    return querys



'''
获取 Query
'''
def get_point(datafile: str, idx: str):
    ids, pois = get_data(datafile)
    id2poi = dict(zip(ids, pois))
    point = tuple(id2poi[idx][1:])
    return point


'''
获取 Query
@return: 
'''
def get_range(filename: str):
    with open(filename, encoding='utf-8') as f:
        all_data = json.load(f)
    ranges = all_data['range']
    return ranges


'''
@param: point1, point2 
@return: dist
'''
def euclidean_dis(p1:tuple, p2:tuple):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2



'''
获取 Query
'''
def k_NN_search(datafile, minheap, query_point, k):
    """
    Parameters:
        minheap: the instance of heap
        query_point: query_point(x,y)
        k: desire number of group size
    Return: a set of RTreeEntry
    """
    s=set()
    min_dis = 0
    tmp = query_point
    global visit_cnt
    while len(s)<k and not minheap.is_empty():
        out=minheap.delete()
        visit_cnt += 1
        if isinstance(out,rtree.RTreeEntry):
            s.add(out.data)
            min_dis = euclidean_dis(query_point, get_point(datafile, int(out.data)))
            tmp = out.data
    if len(s) == k and not minheap.is_empty():
        out = minheap.delete()
        if isinstance(out, rtree.RTreeEntry):
            if min_dis > euclidean_dis(query_point, get_point(datafile, int(out.data))):
                s.remove(tmp)
                s.add(out.data)
    return s



'''
获取 Query
'''
def get_results(datafile:str, POI_id:int, k:int):
    t = RTree()
    # Create an RTree instance with some sample data
    t = RTree(max_entries=7)
    ids, pois = get_data(datafile)
    # ids中存储了所有POI的id编号，pois中以['地点名称', lat, lon]的形式存储了位置信息
    id2poi = dict(zip(ids, pois))
    # print(id2poi)
    for i in range(config_0.index_cnt):
        t.insert(str(ids[i]), Rect(pois[i][1], pois[i][2], pois[i][1], pois[i][2]))

    level=t.get_levels()
    # query POI
    # p = tuple(id2poi[POI_id][1:])
    p=(31.103230943, 121.388255772)
    # build the priority queue of this query
    H = priority_queue.RtreenodeMinheap(p)
    # insert the root node
    H.insert(level[0][0])

    print("===KNN_search===")
    print("The query POI: {}".format(p))

    result=k_NN_search(datafile, H, p, k)
    
    print("The K nearest neighbors set of query is: ", result)
    print("The number of visits to the node is: {}".format(visit_cnt))
    return list(result)

def save_file(ans:dict, filename:str):
    json_str = json.dumps(ans, indent=4)
    with open(filename, 'w') as json_file:
        json_file.write(json_str)


if __name__ == "__main__":
    
    '''
    读取数据
    '''
    datafile = "data/bundle0/dataset.json"
    queryfile = "data/bundle0/task1.json"
    POIresultfile = "result/bundle0/result1.json"


    querys = get_query(queryfile)
    
    results = []
    start_t = time.time()
    
    for i in range(len(querys)):
        results.append(get_results(datafile, querys[i][1], querys[i][0]))
    
    results_dict = {"results":results}
    
    end_t = time.time()
    
    print("The total time on processing {} is: {}s.".format(queryfile, end_t-start_t))
    # save_file(results_dict, POIresultfile)
 
    



