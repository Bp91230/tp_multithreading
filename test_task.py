import unittest

import task


class MyTestCase(unittest.TestCase):
    def test_equal(self):
        a = task.Task(3, 2)
        c = task.Task(2, 2)
        txt = a.to_json()
        b = task.Task.from_json(txt)
        self.assertEqual(a, b)  # add assertion here
        self.assertNotEqual(a, c)


if __name__ == "__main__":
    unittest.main()
