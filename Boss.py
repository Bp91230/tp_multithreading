from QueueClient import QueueClient
from task import Task

# Boss class to send tasks to the minions


class Boss(QueueClient):
    def __init__(self, address, authkey):
        super().__init__(address, authkey)
        self.connect()

    def assign_task(self, task_size, num_times):
        for task_id in range(num_times):
            task_obj = Task(task_size, task_id)
            self.send_task(task_obj)


if __name__ == "__main__":
    boss = Boss("127.0.0.1", b"secret")  # Provide the server's address and authkey
    boss.assign_task(3, 2)  # Assign tasks with size 3, 2 times
