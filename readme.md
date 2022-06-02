## 空间数据库课程实验

### 总体要求说明
- 不使用开源/商业数据库（如MySql或MongoDB等），自行编写程序完成下述任务
- 不限制编程语言，只要能较好支持JSON格式数据即可
- 任务0：
实现一种针对2D空间数据的数据结构，它应拥有增、删、改、查与完成任务1、2的接口
从给定的原始数据集中提取数据，并进行数据的插入
有余力的可以考虑实现数据的落盘（持久化）
- 任务1：
k-NN查询，给定（某个坐标位置，参数k），查询出距离最近的k个POI
- 任务2：
范围查询，给定（矩形区域左下顶点，矩形区域右上顶点），查询出范围内的所有POI
- 最终会使用约定的调用方式进行测试，应尽量提高实现的时空效率
- 如果某个POI恰好在该矩形范围的四个顶点，则也都算作查询结果

- 代码结构没有硬性要求，但请确保在你的代码的根目录下
    + 存在一个名为main的文件作为暴露出的入口
    + 存在一个名为result的文件夹存放query的结果
- 数据集与query文件会存放在与你的代码的根目录同级的data文件夹下
- data文件夹下会有若干个文件夹，每个文件夹名字是[bundle+编号]，内有：
    + 一个数据集文件 dataset.json
    + 任务1的query文件 task1.json和任务2的query文件 task2.json
- 对每个bundle，应把结果放在你的代码的根目录/result/[bundle+编号]下：
任务1的结果文件 result1.json和任务2的结果文件 result2.json

### 任务描述
1. 任务1-query查询
    - 给定某个query的经纬度信息，以及参数k，查询出距离最近的k个POI，具体参见task1.json文件。

2. 任务2-range查询
    - 给定矩形左下顶点的经纬度信息，右上顶点的经纬度信息，查询范围内的所有POI。所有恰好在矩形四个顶点的POI也都算在结果内。

3. 结果格式
    - result.json中会存有对应要求的POI编号集。

### 评价指标
1. 正确率
2. 处理时间
3. 占用内存以及磁盘空间的情况

---
### 代码文件说明
`priority_queue.py`是一个对原始数据进行「索引构建」以及「最小堆构建」
`knn.py`是空间坐标点的最近邻查询样例程序，并且将相关结果写入到结果文件夹
`range_query.py`是


