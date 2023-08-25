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
        # assert
        self.assertEqual(expected, helper.get_all()[0])
