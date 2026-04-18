import pytest
import sys

@pytest.mark.skip(reason="not implemented yet")
def test_db_func():
    assert False

@pytest.mark.skipif(sys.platform=="win32", reason="it does not work on windows")
def test_os_files():
    assert True;

@pytest.mark.parametrize("a,b,p", [(5,3,15), (6,5,30), (2,10,200)])
def test_prod(a,b,p):
    assert a*b==p