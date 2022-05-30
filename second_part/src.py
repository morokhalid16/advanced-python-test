from sys import maxsize

class MySet(set):
    # todo exercise 1
    def __init__(self, L):
        self.L = L

    def __str__(self):
        return (str(set(self.L)))

    def __add__(self, other_MySet):
        res = set.union(set(self.L), set(other_MySet.L))
        return res

    def __sub__(self, other_MySet):
        res = set(self.L).difference(set(other_MySet.L))
        return res
    


        return MySet(self.L)




def decorator_check_max_int(func):
    # todo exercise 2
    def check_max_int(a, b):
        if a + b > maxsize :
            return maxsize

        return func(a, b)


    return check_max_int


@decorator_check_max_int
def add(a, b):
    return a + b


def ignore_exception(my_exception): # e stands for the exception
    def decorator_custom(function): # Décorateur
        def new_function(*args, **kwargs):
              try:
                  return function(*args, **kwargs)
              except my_exception:
                   return 
        return new_function
    return decorator_custom

@ignore_exception(ZeroDivisionError)
def div(a, b):
    return a / b


@ignore_exception(TypeError)
def raise_something(exception):
    raise exception


# exercise 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap


class MetaInherList:
    # todo exercise 5
    pass


class Ex:
    x = 4


class ForceToList(Ex):
    __metaclass__ = MetaInherList
    pass

