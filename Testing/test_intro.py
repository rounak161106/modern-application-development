# Standard naming convention(mandatory)
# Filename : start or end with test_ or _test
# Function name should be started with test keyword
# Class name should start with Testxxxx

#pytest running
# pytest test_intro.py
# pytest .
# pytest test_intro.py -v (Verbose)
# pytest -k "increment"   (k for keyword)
# pytest test_intro.py::test_increment     (Note that test_idtro is file name, increment and test_increment is function name)

def increment(x):
    return x+1;

def test_case1():
    assert increment(4)==5;

def test_case2():
    assert increment(6)==6;
