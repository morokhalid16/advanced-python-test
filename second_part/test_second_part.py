from sys import maxsize
 
import pytest

from src import MySet, div, raise_something, add, ForceToList
from src import CacheDecorator



def test_my_set():
    a = MySet([1, 2, 3])
    b = MySet([1, 5, 100])
    print(a + b)
    assert a + b == {1, 2, 3, 5, 100}
    print(" + operator worsk!")
    print(a - b)
    assert a - b == {2, 3}
    print(" - operator worsk!")


def test_max_int():
    assert add(5, 30) == 35
    print("add(maxsize, 1): ", add(maxsize, 1))
    print("maxsize: ", maxsize)
    assert add(maxsize, 1) == maxsize
    print("test_max_int works!")


def test_ignore_exception():
    assert div(10, 2) == 5
    print(div(10, 2))
    assert div(10, 0) is None
    assert raise_something(TypeError) is None
    with pytest.raises(NotImplementedError):
        raise_something(NotImplementedError)

def test_CacheDecorator():
    cd = CacheDecorator()
    def add(a, b):
        return a+b
    
    print(cd(add)(2,3))
    assert cd(add)(2,3) == 5 # that test passes
    print(add(3,4))


def test_meta_list():
    test = ForceToList([1, 2])
    assert test[1] == 2
    assert test.x == 4

if __name__=="__main__":
    print('Testing MySet:')
    test_my_set()
    print('Testing test_max_int ')
    test_max_int()
    print('Testing ignore_exception ')
    test_ignore_exception()
    print('Testing test_CacheDecorator')
    test_CacheDecorator()