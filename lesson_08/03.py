import inspect


def type_logger(func):
    def wrapper(*args, **kwargs):
        if len(args) > 0:
            p_args = {arg: type(arg)  for arg in args}
            p_args_printable = ", ".join((str(k) + ": " + str(v)) for k, v  in p_args.items())
            print(f"{func.__name__}({p_args_printable})")
        else:
            kwargs_printable = ", ".join((str(k) + ": " + str(v) + " " + str(type(v))) for k, v  in kwargs.items())
            print(f"{func.__name__}({kwargs_printable})")
        res = func(*args, **kwargs)
        return res
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc_2_cubes(x, y):
    return x ** 3, y ** 3


@type_logger
def calc_cube_named(to_cube=0, log_to_stdout=False):
    if log_to_stdout:
        print(f"Called '{inspect.stack()[0][3]}' by '{inspect.stack()[1][3]}'")
    return to_cube ** 3


a = calc_cube(5)
print(a, "\n")
b = calc_2_cubes(5, 6)
print(b, "\n")
c = calc_cube_named(to_cube=7, log_to_stdout=True)
print(c, "\n")
