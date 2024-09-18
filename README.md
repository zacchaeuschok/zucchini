# 🥒 Zucchini

**Zucchini** is a lightweight, Celery-like task queue designed for local development and trialing. It simplifies task management by eliminating the need for external message brokers like Redis or RabbitMQ, making it ideal for rapid prototyping and small-scale applications.

## Features

- **In-Memory Task Queue**: No external dependencies required.
- **Simple API**: Easy-to-use decorators for defining tasks.
- **Multi-threaded Workers**: Execute multiple tasks concurrently.
- **Callback Support**: Handle task results with callbacks.
- **Minimal Setup**: Get started quickly with minimal configuration.
- **Poetry Integration**: Manage dependencies and packaging effortlessly using Poetry.

## Installation

Ensure you have [Poetry](https://python-poetry.org/docs/#installation) installed.

1. **Clone the Repository**

    ```bash
    git clone https://github.com/zacchaeuschok/zucchini.git
    cd zucchini
    ```

2. **Install Dependencies**

    ```bash
    poetry install
    ```

3. **Activate the Virtual Environment**

    ```bash
    poetry shell
    ```

## Usage

### Defining Tasks

Use the `@zucc` decorator to define tasks.

```python
from zucchini import zucc, zq

@zucc
def add(a, b):
    return a + b

@zucc
def multiply(a, b):
    return a * b

if __name__ == "__main__":
    add(5, 7)
    multiply(3, 4)
    
    print("[Example] Waiting for tasks to complete...")
    zq.task_queue.join()  # Wait until all tasks are completed
    zq.shutdown()
    print("[Example] All tasks completed.")
```

### Running the Example

Run the example script using Poetry:

```
poetry run zucchini-example
```

Expected Output:
```
[ZQueue] Started 2 worker(s).
[ZQueue] Task add enqueued with args: (5, 7), kwargs: {}
[ZQueue] Task multiply enqueued with args: (3, 4), kwargs: {}
[ZQueue] Executing task: add with args: (5, 7), kwargs: {}
[ZQueue] Executing task: multiply with args: (3, 4), kwargs: {}
[Example] Waiting for tasks to complete...
[ZQueue] Task add completed with result: 12
[ZQueue] Task multiply completed with result: 12
[ZQueue] All workers have been shut down.
[Example] All tasks completed.
```

### Testing
Run the test suite using Poetry:
```
poetry run pytest
```

### Project Structure

```
zucchini/
├── zucchini/
│   ├── __init__.py
│   ├── queue.py
│   ├── worker.py
│   └── decorators.py
├── examples/
│   └── example.py
├── tests/
│   └── test_zucchini.py
├── pyproject.toml
├── README.md
└── .gitignore
```

### Contributing

Contributions are welcome! Please follow these steps:

1. Fork the Repository 
2. Create a New Branch

```
git checkout -b feature/YourFeature
```

3. Make Your Changes
4. Commit Your Changes

```
git commit -m "Add your message"
```

5. Push to Your Branch

```
git push origin feature/YourFeature
```

6. Open a Pull Request

### License
This project is licensed under the MIT License.

### Acknowledgements
- [Celery](https://docs.celeryq.dev/) for inspiration and ideas.
- [Minikube](https://minikube.sigs.k8s.io/docs/) for local Kubernetes development.
- Built with ❤️ and 🥒 using Python and Poetry.