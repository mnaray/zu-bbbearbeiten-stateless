import helper
import pytest


@pytest.fixture
def setUp():
    helper.clear()


def test_add(setUp):
    # arrange
    expected = helper.Todo("test todo")
    # act
    helper.add(expected.title)
    actual = helper.get(0)
    # assert
    assert expected == actual


def test_update(setUp):
    # arrange
    todo = helper.Todo("test todo")
    helper.add(todo.title)
    expected = helper.Todo("test todo")
    expected.isCompleted = True
    # act
    helper.update(0)
    actual = helper.get(0)
    # assert
    assert expected == actual


def test_bbbisierung(setUp):
    # arrange
    todo = helper.Todo("Babel")
    expected = helper.Todo("Bbbabbbel")
    # act
    helper.add(todo.title)
    actual = helper.get(0)
    # assert
    assert expected == actual
