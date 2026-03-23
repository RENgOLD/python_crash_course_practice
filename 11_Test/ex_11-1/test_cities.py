from city_functions import get_formatted_city_country

def test_city_country():
    assert get_formatted_city_country('santiago','chile') == 'Santiago, Chile'