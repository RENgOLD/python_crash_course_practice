from city_functions import get_formatted_city_country


def test_city_country():
    assert get_formatted_city_country('santiago', 'chile') == 'Santiago, Chile.'


def test_city_country_population():
    assert (get_formatted_city_country(
        'santiago', 'chile', '5000000') ==
            'Santiago, Chile - population 5000000.')
