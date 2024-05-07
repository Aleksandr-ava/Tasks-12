def print_params(a=1, b='aleksandr', c=True):
    print(a, b, c)


print_params()


def print_params(a, b=57, c=46):
    print(a + b + c)


print_params(a=54)


def print_params(a='Ok', b='aleksandr', c=50):
    print(a, b, c)


print_params()


def print_params(a=1, b=25, c=None):
    if c is None:
        c = [1, 2, 3]
    print(a, b, c)


print_params()


def print_params(a, b, c):
    print(a, b, c)


values_list = ['name', 'num', 'bool']
print_params(*values_list)


def print_params(a, b, c):
    print(a, b, c)


values_dict = {'a': 'Aleksandr', 'b': 345, 'c': 'True'}
print_params(**values_dict)


def print_params(a, b, c):
    print(a, b, c)


values_list_2 = ['Aleksandr', 345]
print_params(*values_list_2, 42)
