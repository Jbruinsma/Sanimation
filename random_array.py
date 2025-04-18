import random

def random_array(length, max_value):
    return [random.randint(0, max_value) for val in range(length)]