#!/usr/bin/python
# -*- coding: UTF-8 -*-

from rtreelib import Point


class Poi:
    def __init__(self, index, name, lat, lon):
        self.index = index # 暂存，估计没用
        self.name = name
        self.lat = lat
        self.lon = lon

    def to_string(self):
        """
        输出样例 [1] 苏州大学（37.7，121.1）
        :return:
        """
        return "[" + self.index + "] " + self.name \
               + "（" + self.lat + "，" + self.lon + "）"

    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon

    def get_name(self):
        return self.name

    # TODO：set

    # def get_point(self):
    #     """
    #     Poi -> Point
    #     :return: Point
    #     """
    #     return Point(self.lat, self.lon)




