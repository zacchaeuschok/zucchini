import threading
from queue import Queue, Empty
from typing import Callable, Any, Dict

class Worker:
    def __init__(self, task_queue: Queue, worker_id: int):
        """
        Initialize a Worker instance.

        :param task_queue: The Queue instance to fetch tasks from.
        :param worker_id: Unique identifier for the worker.
        """
        self.task_queue = task_queue
        self.worker_id = worker_id
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.shutdown_flag = threading.Event()

    def start(self):
        """Start the worker thread."""
        print(f"[Worker-{self.worker_id}] Starting worker.")
        self.thread.start()

    def run(self):
        """Continuously fetch and execute tasks from the queue."""
        while not self.shutdown_flag.is_set():
            try:
                task, args, kwargs, callback = self.task_queue.get(timeout=1)
                print(f"[Worker-{self.worker_id}] Executing task: {task.__name__} with args: {args}, kwargs: {kwargs}")
                try:
                    result = task(*args, **kwargs)
                    if callback:
                        callback(result)
                except Exception as e:
                    print(f"[Worker-{self.worker_id}] Task {task.__name__} failed with exception: {e}")
                finally:
                    self.task_queue.task_done()
            except Empty:
                continue

    def stop(self):
        """Signal the worker to shut down and wait for the thread to finish."""
        print(f"[Worker-{self.worker_id}] Stopping worker.")
        self.shutdown_flag.set()
        self.thread.join()
        print(f"[Worker-{self.worker_id}] Worker stopped.")
