import pytest

from mona_vn_normalize import normalize, read_phone


@pytest.mark.parametrize(("value", "expected"), [
    ("1900 636 648", "một chín không không sáu ba sáu sáu bốn tám"),
    ("0909636648", "không chín không chín sáu ba sáu sáu bốn tám"),
    ("+84909636648", "không chín không chín sáu ba sáu sáu bốn tám"),
])
def test_phone(value, expected):
    assert read_phone(value) == expected


@pytest.mark.parametrize(("value", "expected"), [
    ("Tp.HCM", "thành phố Hồ Chí Minh"),
    ("Q.1", "quận một"),
    ("TNHH", "trách nhiệm hữu hạn"),
    ("CLB", "câu lạc bộ"),
    ("TS. An", "tiến sĩ An"),
    ("đ/c 12", "địa chỉ mười hai"),
])
def test_abbreviations(value, expected):
    assert normalize(value) == expected


def test_large_number_is_not_mistaken_for_phone():
    assert normalize("100000000") == "một trăm triệu"
