"""Đọc số La Mã khi có từ khoá ngữ cảnh rõ ràng."""

import re
from .numbers import read_integer

_ROMAN_RE = re.compile(
    r"(?P<context>thế\s+kỷ|kh(?:óa|oá|oa)|quý|chương|kỳ)\s+(?P<roman>[IVXLCDM]+)\b",
    re.IGNORECASE,
)


def roman_to_int(value: str) -> int:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    raw = value.upper()
    if not raw or any(char not in values for char in raw):
        raise ValueError(f"Số La Mã không hợp lệ: {value!r}")
    total = 0
    for index, char in enumerate(raw):
        current = values[char]
        total += -current if index + 1 < len(raw) and current < values[raw[index + 1]] else current
    # Kiểm tra dạng viết chuẩn, tránh nhận nhầm chuỗi chữ cái bất kỳ.
    if int_to_roman(total) != raw:
        raise ValueError(f"Số La Mã không hợp lệ: {value!r}")
    return total


def int_to_roman(value: int) -> str:
    if not 0 < value < 4000:
        raise ValueError("Số La Mã phải từ 1 đến 3999")
    pairs = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
             (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
             (5, "V"), (4, "IV"), (1, "I"))
    parts = []
    for number, token in pairs:
        count, value = divmod(value, number)
        parts.append(token * count)
    return "".join(parts)


def read_roman(value: str) -> str:
    return read_integer(roman_to_int(value))


def normalize_roman(text: str) -> str:
    def replace(match: re.Match) -> str:
        try:
            return f"{match['context']} {read_roman(match['roman'])}"
        except ValueError:
            return match.group()
    return _ROMAN_RE.sub(replace, text)
