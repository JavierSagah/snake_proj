import pytest

@pytest.mark.parametrize('value', [True, False])
def test_my_test(value):
  assert value == True
 
