import pytest

from mona_vn_normalize import read_date, read_time


@pytest.mark.parametrize(("value", "expected"), [
    ("15/09/2026", "ngày mười lăm tháng chín năm hai nghìn không trăm hai mươi sáu"),
    ("2/9", "ngày mùng hai tháng chín"),
    ("2/9/2026", "ngày hai tháng chín năm hai nghìn không trăm hai mươi sáu"),
    ("12/12/24", "ngày mười hai tháng mười hai năm hai nghìn không trăm hai mươi tư"),
])
def test_date(value, expected):
    assert read_date(value) == expected


@pytest.mark.parametrize(("value", "expected"), [
    ("14:30", "mười bốn giờ ba mươi phút"),
    ("9h30", "chín giờ ba mươi phút"),
    ("9g30", "chín giờ ba mươi phút"),
    ("9h", "chín giờ"),
])
def test_time(value, expected):
    assert read_time(value) == expected


def test_invalid_date():
    with pytest.raises(ValueError):
        read_date("32/13")


def test_existing_date_word_is_not_duplicated():
    from mona_vn_normalize import normalize
    assert normalize("ngày 15/09/2026") == "ngày mười lăm tháng chín năm hai nghìn không trăm hai mươi sáu"
