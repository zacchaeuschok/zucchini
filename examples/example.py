from zucchini import zucc, zq
import time


@zucc
def add(a, b):
    time.sleep(2)
    return a + b


@zucc
def multiply(a, b):
    time.sleep(3)
    return a * b


def main():
    add(5, 7)
    multiply(3, 4)

    print("[Example] Waiting for tasks to complete...")
    zq.task_queue.join()
    zq.shutdown()
    print("[Example] All tasks completed.")


if __name__ == "__main__":
    main()
