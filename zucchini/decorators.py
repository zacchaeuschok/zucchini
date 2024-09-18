# zucchini/decorators.py
from functools import wraps
from typing import Callable, Any, Optional
from .queue import ZQueue

zq = ZQueue()
zq.start_worker(worker_count=2)


def zucc(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        callback: Optional[Callable[[Any], None]] = kwargs.pop('callback', None)

        def default_callback(result):
            print(f"[ZQueue] Task {func.__name__} completed with result: {result}")

        if callback is None:
            callback = default_callback

        zq.enqueue(func, args, kwargs, callback)

    return wrapper
