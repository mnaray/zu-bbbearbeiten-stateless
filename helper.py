from dataclasses import dataclass
import datetime
import operator

# In dieser Variable werden die Daten gespeichert. (Im Arbeitsspeicher)
todos = []


@dataclass
class Category:
    name: str
    id: int


categories = [
    Category("Overall", 0),
    Category("School", 1),
    Category("Work", 2),
    Category("Chores", 3),
]


@dataclass
class Todo:
    title: str
    date: datetime.datetime
    category: Category
    description: str = "no description"
    isCompleted: bool = False

    def __init__(
        self, _title, _date, _category=categories[0], _description="no description"
    ):
        self.title = _title
        self.date = datetime.datetime.strptime(_date, "%Y-%m-%d")
        self.category = _category
        self.description = _description


# Hier findet die Ver-BBB-isierung statt.
def add(title, date, category=categories[0], description="no description"):
    title = title.replace("b", "bbb").replace("B", "Bbb")
    todos.append(Todo(title, date, category, description))
    todos.sort(key=operator.attrgetter("date"))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted


def get_csv():
    csv = ""
    for todo in todos:
        csv += f"{todo.title},{todo.date},{todo.category.name},{todo.description},{todo.isCompleted}"
        if not todos.index(todo) == len(todos) - 1:
            csv += "\n"
    return csv


def clear():
    todos.clear()
