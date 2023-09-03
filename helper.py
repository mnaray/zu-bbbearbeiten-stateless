import datetime
import operator
from dataclasses import dataclass

items = []


@dataclass
class Item:
    text: str
    date: datetime
    description: str
    isCompleted: bool = False


def oneWeekFromToday():
    today = datetime.datetime.now()
    oneWeek = datetime.timedelta(weeks=1)
    return today + oneWeek


def add(text, date=None, description=None):
    text = text.replace("b", "bbb").replace("B", "Bbb")

    if date is None:
        date = oneWeekFromToday()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")

    items.append(Item(text, date, description))
    items.sort(key=lambda x: x.date)


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
