import pytest

@pytest.mark.smoke
def test_case1():
    assert False

@pytest.mark.slow
def test_case2():
    assert True;

@pytest.mark.web
def test_case3(a,b,p):
    assert a*b==p

@pytest.mark.recursion
def test_case5(a,b,p):
    assert a*b==p

@pytest.mark.smoke
def test_case4(a,b,p):
    assert a*b==p

# pytest test_intro5.py -m slow (means only func with slow markup will be tested)
# pytest test_intro5.py -m smoke (means all func. with this markup ie. smoke will be selected)
