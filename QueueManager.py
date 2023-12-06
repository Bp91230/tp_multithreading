import multiprocessing
from multiprocessing.managers import BaseManager


# QueueManager class to manage the task and result queues
class QueueManager(BaseManager):
    def __init__(self, address, authkey):
        super().__init__(address=address, authkey=authkey)
        self.task_queue = multiprocessing.Queue()
        self.result_queue = multiprocessing.Queue()


if __name__ == "__main__":
    # Create a multiprocessing manager and queues
    manager = QueueManager(address=("127.0.0.1", 50000), authkey=b"secret")
    manager.start()

    # Get the server object
    server = manager.get_server()
    server.serve_forever()
