# !/usr/bin/env python
# -*- coding:utf-8 -*-

from Queue import Queue
from collections import deque


class SetUniqueQueue(Queue):
    """
    扩展Queue实现集合功能，但是会失去FIFO特性.
    Queue源代码https://github.com/python/cpython/blob/master/Lib/queue.py#L21
    stackoverflow 相关讨论：
    http://stackoverflow.com/questions/16506429/check-if-element-is-already-in-a-queue/16506527#16506527
    http://stackoverflow.com/questions/1581895/how-check-if-a-task-is-already-in-python-queue
    我采用了双倍的空间占用来解决FIFO，即同时采用set与deque。
    deque用于保存顺序，set用于保证无重复.
    在这个情景中，时间花销比空间花销更重要.
    """
    # def put(self, item, block=True, timeout=None):
    #     if item not in self.queue: # fix join bug
    #         Queue.put(self, item, block, timeout)

    def _init(self, maxsize):
        self.queue = deque()
        self.setqueue = set()

    def _put(self, item):
        # todo:更优的做法？
        if item not in self.setqueue:
            self.setqueue.add(item)
            self.queue.append(item)

    def _get(self):
        return self.queue.popleft()
