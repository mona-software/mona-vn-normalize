"""Chuẩn hoá văn bản tiếng Việt cho TTS và NLP."""

from .abbrev import normalize_abbreviations, read_abbreviation
from .currency import normalize_currency, read_currency
from .datetime_vn import normalize_dates, normalize_times, read_date, read_time
from .numbers import normalize_numbers, read_integer, read_number
from .phone import normalize_phones, read_phone
from .roman import normalize_roman, read_roman, roman_to_int
from .text import clean_text
from .units import normalize_units, read_unit

__version__ = "0.1.0"


def normalize(
    text: str,
    *,
    currency: bool = True,
    phone: bool = True,
    dates: bool = True,
    times: bool = True,
    numbers: bool = True,
    units: bool = True,
    abbrev: bool = True,
    roman: bool = True,
) -> str:
    """Chuẩn hoá văn bản theo pipeline an toàn cho các token chồng lấn."""
    if not isinstance(text, str):
        raise TypeError("text phải là chuỗi")
    if currency:
        text = normalize_currency(text)
    if phone:
        text = normalize_phones(text)
    if dates:
        text = normalize_dates(text)
    if times:
        text = normalize_times(text)
    if abbrev:
        text = normalize_abbreviations(text)
    if roman:
        text = normalize_roman(text)
    if units:
        text = normalize_units(text)
    if numbers:
        text = normalize_numbers(text)
    return clean_text(text)


__all__ = [
    "normalize", "read_number", "read_integer", "read_currency", "read_date",
    "read_time", "read_phone", "read_abbreviation", "read_unit", "read_roman",
    "roman_to_int", "clean_text",
]

