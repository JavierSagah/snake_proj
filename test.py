import pytest

@pytest.mark.parametrize('value', [True, False])
def my_test(value):
  assert value == True
 
