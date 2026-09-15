import pytest

from mona_vn_normalize import clean_text, normalize, read_roman, roman_to_int


@pytest.mark.parametrize(("value", "expected"), [
    ("25°C", "hai mươi lăm độ C"),
    ("50%", "năm mươi phần trăm"),
    ("10km", "mười ki lô mét"),
    ("5kg", "năm ki lô gam"),
    ("20m2", "hai mươi mét vuông"),
    ("3m³", "ba mét khối"),
    ("2 + 3 = 5", "hai cộng ba bằng năm"),
    ("5-2", "năm trừ hai"),
])
def test_units(value, expected):
    assert normalize(value) == expected


@pytest.mark.parametrize(("value", "expected"), [
    ("thế kỷ XXI", "thế kỷ hai mươi mốt"),
    ("khoá VII", "khoá bảy"),
    ("Chương IV", "Chương bốn"),
    ("Quý III", "Quý ba"),
])
def test_roman_in_context(value, expected):
    assert normalize(value) == expected


def test_roman_without_context_is_untouched():
    assert normalize("Áo size XL") == "Áo size XL"


def test_roman_conversion():
    assert roman_to_int("MCMXCIX") == 1999
    assert read_roman("IX") == "chín"


def test_text_cleanup_preserves_vietnamese():
    assert clean_text("  Tiếng   Việt , rất đẹp!  ") == "Tiếng Việt, rất đẹp!"


def test_feature_flag_and_pipeline_sentence():
    assert normalize("Giá 500k lúc 9h30.") == "Giá năm trăm nghìn đồng lúc chín giờ ba mươi phút."
    assert normalize("Mã 123", numbers=False) == "Mã 123"


def test_non_string_rejected():
    with pytest.raises(TypeError):
        normalize(123)
