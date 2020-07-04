import pytest
import datetime
from tasks import Task
from tasks import Tasks


class TestTomorrowTaskList():
    def test_empty(self):
        task_list = Tasks()
        assert task_list.tomorrow() == []

    def test_filters_other_days(self):
        task_list = Tasks()
        task_list.add_task(Task("do the laundry"))
        next_week = datetime.date.today() + datetime.timedelta(days=7)
        task_list.add_task(Task("important meeting", date=next_week))
        assert task_list.tomorrow() == []

    def test_finds_tomorrows_tasks(self):
        task_list = Tasks()
        next_week = datetime.date.today() + datetime.timedelta(days=7)
        task_list.add_task(Task("important meeting", date=next_week))
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        task_list.add_task(Task("John's birthday", date=tomorrow))

        result = task_list.tomorrow()
        assert len(result) == 1
        assert result[0].title == "John's birthday"

    def test_today(self):
        task_list = Tasks()  # create an object of the class
        task_list.add_task(Task('Party', date=datetime.date.today()))
        result = task_list.today()
        assert result[0].title == 'Party'
