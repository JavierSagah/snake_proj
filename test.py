import pytest

@pytest.mark.parametrize('value', [True, False])
def test_my_test1(value):
  assert value == True

  
def test_my_test2():
  assert True == True

  
def test_my_test3():
  assert True == False
