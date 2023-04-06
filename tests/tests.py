import pytest
import random

a = random.randint(1, 3)
def random_test(x):
    assert x == a

if __name__ == '__main__':
    random_test(a)