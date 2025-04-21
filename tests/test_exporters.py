from wexp.exporters import get_country_by_id
from wexp.load_data import load_data


load_data()


def test_countries_exist():
    assert "USA" == get_country_by_id(1201).Name
    assert "China" == get_country_by_id(1202).Name
    assert "India" == get_country_by_id(1203).Name
    assert "Australia" == get_country_by_id(1204).Name
