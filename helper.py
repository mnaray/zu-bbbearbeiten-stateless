from dataclasses import dataclass
import datetime
import operator

# In dieser Variable werden die Daten gespeichert. (Im Arbeitsspeicher)
todos = []


@dataclass
class Todo:
    title: str
    date: datetime.datetime
    description: str = "no description"
    isCompleted: bool = False

    def __init__(self, _title, _date, _description="no description"):
        self.title = _title
        self.date = datetime.datetime.strptime(_date, "%Y-%m-%d")
        self.description = _description


# Hier findet die Ver-BBB-isierung statt.
def add(title, date, description="no description"):
    title = title.replace("b", "bbb").replace("B", "Bbb")
    todos.append(Todo(title, date, description))
    todos.sort(key=operator.attrgetter("date"))
    # todos.sort(key=lambda o: o.date)


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted


def clear():
    todos.clear()
