from QueueManager import QueueManager

# QueueClient class to interact with the task and result queues


class QueueClient:
    def __init__(self, address, authkey):
        self.address = address
        self.authkey = authkey
        self.task_queue = None
        self.result_queue = None

    def connect(self):
        QueueManager.register("get_tasks")
        QueueManager.register("get_results")

        manager = QueueManager(address=(self.address, 5000), authkey=self.authkey)
        manager.connect()

        self.task_queue = manager.get_tasks()
        self.result_queue = manager.get_results()

    def send_task(self, task):
        self.task_queue.put(task)

    def get_result(self):
        return self.result_queue.get()
