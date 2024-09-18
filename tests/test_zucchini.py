# tests/test_zucchini.py
import unittest
from zucchini import zucc, zq


class TestZucchini(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Called once before all tests.
        Ensures that workers are already started by the global ZQueue instance.
        """
        pass  # Workers are started in decorators.py upon ZQueue initialization

    def setUp(self):
        """
        Called before each test.
        Resets the result for each test case.
        """
        self.result = None

    def test_add_task(self):
        """
        Test the 'add' task to ensure it correctly adds two numbers.
        """

        @zucc
        def add(a, b):
            return a + b

        def callback(result):
            self.result = result

        add(2, 3, callback=callback)  # Pass the custom callback
        zq.task_queue.join()  # Wait until the task is processed
        self.assertEqual(self.result, 5)

    def test_multiply_task(self):
        """
        Test the 'multiply' task to ensure it correctly multiplies two numbers.
        """

        @zucc
        def multiply(a, b):
            return a * b

        def callback(result):
            self.result = result

        multiply(4, 5, callback=callback)  # Pass the custom callback
        zq.task_queue.join()  # Wait until the task is processed
        self.assertEqual(self.result, 20)

    @classmethod
    def tearDownClass(cls):
        """
        Called once after all tests.
        Shuts down the global ZQueue instance to terminate workers.
        """
        zq.shutdown()


if __name__ == '__main__':
    unittest.main()
