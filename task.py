from time import perf_counter

import numpy as np


class Task:
    def __init__(self, _size, _id):
        self.identifier = _id
        self.x = 0
        self.a = 0
        self.b = 0
        self.time = 0
        self.size = _size

    def work(self):
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        start = perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        end = perf_counter()
        self.time = end - start
