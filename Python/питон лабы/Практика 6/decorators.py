from functools import wraps
from time import perf_counter
from models import Status


def log(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Вызов:", function.__name__)
        return function(*args, **kwargs)
    return wrapper


def timed(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        print(f"Время {function.__name__}: {perf_counter() - start:.6f} с")
        return result
    return wrapper


def require_status(status: Status):
    def decorate(function):
        @wraps(function)
        def wrapper(self, delivery, *args, **kwargs):
            if delivery.status != status:
                raise ValueError("Недопустимый статус для операции")
            return function(self, delivery, *args, **kwargs)
        return wrapper
    return decorate
