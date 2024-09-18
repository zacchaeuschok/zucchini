import queue
from typing import Callable, Any, Dict
from .worker import Worker

class ZQueue:
    def __init__(self):
        self.task_queue = queue.Queue()
        self.workers = []
        self.worker_id_counter = 1

    def start_worker(self, worker_count: int = 1):
        """
        Start a specified number of worker threads.

        :param worker_count: Number of workers to start.
        """
        for _ in range(worker_count):
            worker = Worker(self.task_queue, self.worker_id_counter)
            worker.start()
            self.workers.append(worker)
            self.worker_id_counter += 1
        print(f"[ZQueue] Started {worker_count} worker(s).")

    def enqueue(self, task: Callable, args: tuple, kwargs: Dict[str, Any], callback: Callable = None):
        """
        Add a task to the queue.

        :param task: The callable task to execute.
        :param args: Positional arguments for the task.
        :param kwargs: Keyword arguments for the task.
        :param callback: Optional callback to handle the task result.
        """
        self.task_queue.put((task, args, kwargs, callback))
        print(f"[ZQueue] Task {task.__name__} enqueued with args: {args}, kwargs: {kwargs}")

    def shutdown(self):
        """Shut down all workers gracefully."""
        print("[ZQueue] Shutting down all workers...")
        for worker in self.workers:
            worker.stop()
        print("[ZQueue] All workers have been shut down.")
