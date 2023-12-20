import multiprocessing
from multiprocessing.managers import BaseManager


# QueueManager class to manage the task and result queues
class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    # Create multiprocessing Queues for tasks and results
    task_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()

    # Register task and result queues with the QueueManager
    QueueManager.register("get_tasks", callable=lambda: task_queue)
    QueueManager.register("get_results", callable=lambda: result_queue)
    manager = QueueManager(address=("localhost", 5000), authkey=b"secret")
    # manager.start()

    # Get the server object
    server = manager.get_server()
    print("server ready !")
    server.serve_forever()
