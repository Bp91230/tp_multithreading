from QueueClient import QueueClient


# Minion class to receive and execute tasks
class Minion(QueueClient):
    def __init__(self, address, authkey):
        super().__init__(address, authkey)
        self.connect()

    def start_working(self):
        while True:
            print("Waiting for task ...")
            task = self.task_queue.get()

            print(f"Task {task.identifier} received")
            task.work()

            self.result_queue.put(
                f"Task {task.identifier} completed in {task.time} seconds"
            )
            print("result sent ... ")


if __name__ == "__main__":
    minion = Minion("localhost", b"secret")  # Provide the server's address and authkey
    minion.start_working()
