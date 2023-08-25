import unittest
import helper


class TestModelMethods(unittest.TestCase):
    def setUp(self):
        helper.clear()

    def test_add(self):
        # arrange
        expected = helper.Todo("test todo")
        # act
        helper.add(expected.title)
        actual = helper.get(0)
        # assert
        self.assertEqual(expected, actual)

    def test_update(self):
        # arrange
        todo = helper.Todo("test todo")
        helper.add(todo.title)
        expected = helper.Todo("test todo")
        expected.isCompleted = True
        # act
        helper.update(0)
        actual = helper.get(0)
        # assert
        self.assertEqual(expected, actual)
