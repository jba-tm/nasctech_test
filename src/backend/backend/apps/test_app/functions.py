def get_sum(x):
    return sum(x)

def get_twice_sum(x):
    return sum(x)*2

def get_average(x):
    return sum(x) / len(x)


def get_length(x):
    return len(x)


def get_max(x):
    return max(x)


def get_min(x):
    return min(x)


functions = {
    'sum': get_sum,
    'twice_sum': get_twice_sum,
    'average': get_average,
    'length': get_length,
    'max': get_max,
    'min': get_min,
}
