import datetime
import pytest
from task2 import Homework, DeadlineError, Student, HomeworkResult, Teacher

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
    assert isinstance(student.do_homework('solution', homework), HomeworkResult)
    expired_homework = Homework(text, datetime.timedelta(seconds=0))
    with pytest.raises(DeadlineError):
        student.do_homework('solution', expired_homework)

def test_homework_result_init(student):
    text = 'Learn functions'
    deadline_days = 3
    deadline = datetime.timedelta(days=deadline_days)
    homework = Homework(text, deadline)
    result = student.do_homework('solution', homework)
    assert result.author == student
    assert result.homework == homework
    assert result.solution == 'solution'
    assert result.created == homework.created

def test_check_homework(teacher, student):
    text = 'Learn functions'
    deadline_days = 3
    deadline = datetime.timedelta(days=deadline_days)
    homework = teacher.create_homework(text, deadline_days)
    result = student.do_homework('solution', homework)
    assert teacher.check_homework(result) is True
    assert teacher.homework_done[homework] == 'solution'
    assert teacher.check_homework(HomeworkResult(student, homework, 'sol')) is False

def test_reset_results(teacher):
    text = 'Learn functions'
    deadline_days = 3
    deadline = datetime.timedelta(days=deadline_days)
    homework = teacher.create_homework(text, deadline_days)
    teacher.check_homework(HomeworkResult(Student('Roman', 'Petrov'), homework, 'solution'))
    teacher.reset_results(homework)
    assert teacher.homework_done[homework] is None
    teacher.check_homework(HomeworkResult(Student('Roman', 'Petrov'), homework, 'solution'))
    teacher.reset_results()
    assert teacher.homework_done == {}

