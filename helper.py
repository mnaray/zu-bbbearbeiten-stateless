from dataclasses import dataclass

# In dieser Variable werden die Daten gespeichert. (Im Arbeitsspeicher)
todos = []


@dataclass
class Todo:
    title: str
    isCompleted: bool = False


# Hier findet die Ver-BBB-isierung statt.
def add(title):
    title = title.replace("b", "bbb").replace("B", "Bbb")
    todos.append(Todo(title))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted


def clear():
    todos.clear()


if __name__ == "__main__":
    unittest.main()
