import pytest

from mona_vn_normalize import read_currency


@pytest.mark.parametrize(("value", "expected"), [
    ("500k", "năm trăm nghìn đồng"),
    ("2tr", "hai triệu đồng"),
    ("1,5 triệu", "một triệu năm trăm nghìn đồng"),
    ("150.000đ", "một trăm năm mươi nghìn đồng"),
    ("1 tỷ", "một tỷ đồng"),
    ("250000 VND", "hai trăm năm mươi nghìn đồng"),
    ("2 triệu đồng", "hai triệu đồng"),
])
def test_currency(value, expected):
    assert read_currency(value) == expected
