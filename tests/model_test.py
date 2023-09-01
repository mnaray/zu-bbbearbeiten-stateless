import helper
import pytest

date = "2023-09-02"


@pytest.fixture
def setUp():
    helper.clear()


def test_update(setUp):
    # arrange
    todo = helper.Todo("test todo", date)
    helper.add(todo.title, date)
    expected = helper.Todo("test todo", date)
    expected.isCompleted = True
    # act
    helper.update(0)
    actual = helper.get(0)
    # assert
    assert expected == actual


def test_bbbisierung(setUp):
    # arrange
    todo = helper.Todo("Babel", date)
    expected = helper.Todo("Bbbabbbel", date)
    # act
    helper.add(todo.title, date)
    actual = helper.get(0)
    # assert
    assert expected == actual
