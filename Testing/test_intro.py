# Standard naming convention
# Filename : start or end with test_ or _test
# Function name should be started with test keyword
# Class name should start with Testxxxx

#pytest running
# pytest test_intro.py
# pytest .
# pytest test_intro.py -v (Verbose)
# pytest -k "increment"
# pytest test_intro.py::test_increment

def increment(x):
    return x+1;

def test_case1():
    assert increment(4)==5;
