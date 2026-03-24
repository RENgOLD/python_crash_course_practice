import pytest
from employee import Employee

@pytest.fixture()
def the_employee():
    the_employee = Employee('firstname','lastname','10000')
    return the_employee

def test_give_default_raise(the_employee):
    the_employee.give_raise()
    assert the_employee.salary == 15000

def test_give_custom_raise(the_employee):
    the_employee.give_raise(8000)
    assert the_employee.salary == 18000