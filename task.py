import json
from time import perf_counter

import numpy as np


class Task:
    def __init__(self, _size=3, _id=0):
        self.identifier = _id
        self.size = _size
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        self.x = np.zeros(self.size)
        self.time = 0

    def work(self):
        start = perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        end = perf_counter()
        self.time = end - start

    def to_json(self):
        taskInfo = {
            "identifier": self.identifier,
            "time": self.time,
            "size": self.size,
            "a": self.a.tolist(),
            "b": self.b.tolist(),
            "x": self.x.tolist(),
        }
        return json.dumps(taskInfo)

    def from_json(text: str):
        task = Task()
        taskInfo = json.loads(text)
        task.identifier = taskInfo["identifier"]
        task.size = taskInfo["size"]
        task.time = taskInfo["time"]
        task.a = np.array(taskInfo["a"])
        task.b = np.array(taskInfo["b"])
        task.x = np.array(taskInfo["x"])
        return task

    def __eq__(self, other: "Task"):
        if not isinstance(other, Task):
            return False
        test = True
        if self.identifier != other.identifier:
            test = False
        if self.time != other.time:
            test = False
        if self.size != other.size:
            test = False
        if not np.array_equal(self.a, other.a):
            test = False
        if not np.array_equal(self.b, other.b):
            test = False
        if not np.array_equal(self.x, other.x):
            test = False

        return test
