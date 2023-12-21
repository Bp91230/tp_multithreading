from QueueClient import QueueClient
from task import Task

# Boss class to send tasks to the minions


class Boss(QueueClient):
    def __init__(self, address, authkey):
        super().__init__(address, authkey)
        self.result = None
        self.connect()

    def assign_task(self, task_size, num_times):
        for task_id in range(num_times):
            task_obj = Task(task_size, task_id)
            self.send_task(task_obj)
            print(f"Task {task_id} added to the queue.")
            self.result = self.get_result()
            while self.result is None:
                self.result = self.get_result()
            print(self.result)


if __name__ == "__main__":
    boss = Boss("localhost", b"secret")  # Provide the server's address and authkey
    boss.assign_task(3000, 3)  # Assign tasks with size 3000, 3 times
