from dataclasses import dataclass

# In dieser Variable werden die Daten gespeichert. (Im Arbeitsspeicher)
items = []


@dataclass
class Item:
    text: str
    isCompleted: bool = False

# Hier findet die Ver-BBB-isierung statt.
def add(text):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    items.append(Item(text))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
