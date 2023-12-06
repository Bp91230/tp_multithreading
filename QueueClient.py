from QueueManager import QueueManager

# QueueClient class to interact with the task and result queues


class QueueClient:
    def __init__(self, address, authkey):
        self.address = address
        self.authkey = authkey
        self.task_queue = None
        self.result_queue = None

    def connect(self):
        QueueManager.register("task_queue")
        QueueManager.register("result_queue")

        manager = QueueManager(address=(self.address, 50000), authkey=self.authkey)
        manager.connect()

        self.task_queue = manager.task_queue()
        self.result_queue = manager.result_queue()

    def send_task(self, task):
        self.task_queue.put(task)

    def get_result(self):
        return self.result_queue.get()
