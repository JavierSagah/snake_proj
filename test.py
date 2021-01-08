import pytest

@pytest.mark.parametrize('value', [true, false])
def my_test(value):
  assert value == true
 
