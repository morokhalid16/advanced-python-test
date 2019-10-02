from sys import maxsize

import pytest

from second_part.src import MySet, div, raise_something, add, ForceToList


def test_my_set():
    a = MySet([1, 2, 3])
    b = MySet([1, 5, 100])
    assert a + b == {1, 2, 3, 5, 100}
    assert a - b == {2, 3}


def test_max_int():
    assert add(5, 30) == 35
    assert add(maxsize, 1) == maxsize


def test_ignore_exception():
    assert div(10, 2) == 5
    assert div(10, 0) is None
    assert raise_something(TypeError) is None
    with pytest.raises(NotImplementedError):
        raise_something(NotImplementedError)


def test_meta_list():
    test = ForceToList([1, 2])
    assert test[1] == 2
    assert test.x == 4

