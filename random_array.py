import random

def random_array(length : int, max_value : int) -> list[int]:
    return [random.randint(0, max_value) for val in range(length)]