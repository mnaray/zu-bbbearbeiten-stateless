import pytest
import helper
import datetime


@pytest.fixture
def setUp():
    helper.clear()


def test_add(setUp):
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date)

    # Then: The most recently added to-do should have a date
    item = helper.get_all()[-1]
    assert isinstance(item.date, datetime.date)


def test_sort(setUp):
    # Given: I have several to-dos with dates
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ("Sinn des Lebens entdecken", "2023-09-01"),
        ("Superheld werden", "2023-10-25"),
        ("Netto null", "2050-01-01"),
    ]

    # When: I add the todos
    for todo in todos:
        helper.add(todo[0], todo[1])

    # Then: They should be sorted by date
    for i in range(len(helper.todos) - 1):
        assert helper.todos[i].date < helper.todos[i + 1].date


def test_cat(setUp):
    todos = [
        ("Universum debuggen", "2023-09-06", helper.categories[1]),
        ("Superheld werden", "2023-10-25", helper.categories[3]),
        ("Netto null", "2050-01-01"),
    ]

    for todo in todos:
        if len(todo) == 3:
            helper.add(todo[0], todo[1], todo[2])
        elif len(todo) == 2:
            helper.add(todo[0], todo[1])

    assert helper.todos[0].category.name == "School"
    assert helper.todos[1].category.name == "Chores"
    assert helper.todos[2].category.name == "Overall"
