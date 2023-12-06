from QueueClient import QueueClient


# Minion class to receive and execute tasks
class Minion(QueueClient):
    def __init__(self, address, authkey):
        super().__init__(address, authkey)
        self.connect()

    def start_working(self):
        while True:
            task = self.task_queue.get()
            if task is None:
                break  # Exit loop when a None task is received

            task.work()
            self.result_queue.put(
                f"Task {task.identifier} completed in {task.time} seconds"
            )


if __name__ == "__main__":
    minion = Minion("127.0.0.1", b"secret")  # Provide the server's address and authkey
    minion.start_working()
