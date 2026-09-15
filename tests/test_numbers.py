import pytest

from mona_vn_normalize.numbers import read_number


@pytest.mark.parametrize(("value", "expected"), [
    (0, "không"),
    (1, "một"),
    (15, "mười lăm"),
    (21, "hai mươi mốt"),
    (24, "hai mươi tư"),
    (100, "một trăm"),
    (105, "một trăm lẻ năm"),
    (1000, "một nghìn"),
    (1234, "một nghìn hai trăm ba mươi tư"),
    (1_000_000, "một triệu"),
    (1_500_000, "một triệu năm trăm nghìn"),
    (2026, "hai nghìn không trăm hai mươi sáu"),
    (-12, "âm mười hai"),
    ("12,5", "mười hai phẩy năm"),
])
def test_read_number(value, expected):
    assert read_number(value) == expected


def test_invalid_number():
    with pytest.raises(ValueError):
        read_number("mười")

