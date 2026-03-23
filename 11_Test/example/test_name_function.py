from name_function import get_formatted_name

def test_first_last_name():
    assert get_formatted_name('first', 'last') == 'First Last'

def test_first_last_middle_name():
    assert get_formatted_name('first','last','middle') == 'First Middle Last'
