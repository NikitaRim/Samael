import datetime
import pytest

from task1 import Homework, Student, Teacher


@pytest.fixture
def teacher():
    return Teacher('Daniil', 'Shadrin')


@pytest.fixture
def student():
    return Student('Roman', 'Petrov')


def test_homework_init():
    text = 'Learn functions'
    deadline = datetime.timedelta(days=1)
    created = datetime.datetime.now()
    homework = Homework(text, deadline)
    assert homework.text == text
    assert homework.deadline == deadline
    assert (homework.created - created).total_seconds() < 1


def test_homework_is_active():
    text = 'Learn functions'
    deadline = datetime.timedelta(days=1)
    homework = Homework(text, deadline)
    assert homework.is_active() is True
    expired_homework = Homework(text, datetime.timedelta(seconds=0))
    assert expired_homework.is_active() is False


def test_student_init(student):
    assert student.last_name == 'Petrov'
    assert student.first_name == 'Roman'


def test_teacher_init(teacher):
    assert teacher.last_name == 'Shadrin'
    assert teacher.first_name == 'Daniil'


def test_create_homework(teacher):
    text = 'Learn functions'
    deadline_days = 3
    deadline = datetime.timedelta(days=deadline_days)
    homework = teacher.create_homework(text, deadline_days)
    assert homework.text == text
    assert homework.deadline == deadline


def test_do_homework(student):
    text = 'Learn functions'
    deadline_days = 3
    deadline = datetime.timedelta(days=deadline_days)
    homework = Homework(text, deadline)
    assert student.do_homework(homework) == homework
    expired_homework = Homework(text, datetime.timedelta(seconds=0))
    assert student.do_homework(expired_homework) is None