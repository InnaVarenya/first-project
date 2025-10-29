import functools


def log(filename=None):
   """Декоратор для логирования начала, конца и ошибок выполнения функции"""
    def decorator(func):
       """Декоратор-обертка, принимающая функцию для логирования"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Функциия, выполняющая логирование перед и после вызова функции,
             а также при возникновении ошибки"""
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                error_type = type(e).__name__
                inputs_repr = (args, kwargs)
                error_message = f"{func.__name__} error: {error_type}. Inputs: {inputs_repr}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
                raise
        return wrapper
    return decorator
