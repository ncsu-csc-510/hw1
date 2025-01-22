import pytest
import myfile

# pytest discovers functions with 'test_' as a prefix

def test_pass():
    assert myfile.factorial(3) == 6

def test_fail():
    assert myfile.factorial(-1) == 1

