from task4 import instances_counter, User
import pytest


def test_instances_counter():
    assert User.get_created_instances() == 0
    user1, user2 = User(), User()
    assert user2.get_created_instances() == 0
    assert user1.reset_instances_counter() == 0
    assert User.get_created_instances() == 0


def test_instances_counter_multiple_classes():
    @instances_counter
    class MyClass:
        pass

    @instances_counter
    class AnotherClass:
        pass

    assert MyClass.get_created_instances() == 0
    assert AnotherClass.get_created_instances() == 0
    obj1 = MyClass()
    obj2 = MyClass()
    obj3 = AnotherClass()
    assert obj1.get_created_instances() == 2
    assert obj3.get_created_instances() == 1
    assert MyClass.get_created_instances() == 2
    assert AnotherClass.get_created_instances() == 1
    assert obj2.reset_instances_counter() == 2
    assert obj3.reset_instances_counter() == 1
    assert MyClass.get_created_instances() == 0
    assert AnotherClass.get_created_instances() == 0


if __name__ == '__main__':
    pytest.main()

