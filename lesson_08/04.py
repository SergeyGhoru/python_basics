ERR_NEGATIVE_ARG = "Given a negative argument"


def val_checker(rule):
    def decor(func):
        def wrapper(*args, **kwargs):
            if rule(args[0]):
                res = func(*args, **kwargs)
                return res
            else:
                raise ValueError(ERR_NEGATIVE_ARG)
        return wrapper
    return decor


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print("\n")
print(calc_cube(-5))
