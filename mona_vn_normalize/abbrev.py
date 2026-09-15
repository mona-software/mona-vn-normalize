"""Mở rộng các chữ viết tắt tiếng Việt phổ biến."""

import re
from .numbers import read_integer

_PHRASES = (
    (r"Tp\.?\s*HCM", "thành phố Hồ Chí Minh"),
    (r"TP\.?\s*HCM", "thành phố Hồ Chí Minh"),
    (r"đ/c", "địa chỉ"),
    (r"ThS\.?", "thạc sĩ"),
    (r"TS\.?", "tiến sĩ"),
    (r"TNHH", "trách nhiệm hữu hạn"),
    (r"CLB", "câu lạc bộ"),
    (r"UBND", "ủy ban nhân dân"),
)


def normalize_abbreviations(text: str) -> str:
    text = re.sub(
        r"(?<!\w)Q\.\s*(\d+)",
        lambda match: "quận " + read_integer(int(match.group(1))),
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"(?<!\w)P\.(?=\s|\d|$)", "phường ", text, flags=re.IGNORECASE)
    for pattern, replacement in _PHRASES:
        text = re.sub(rf"(?<!\w){pattern}(?!\w)", replacement, text, flags=re.IGNORECASE)
    return text


def read_abbreviation(value: str) -> str:
    result = normalize_abbreviations(value).strip()
    if result.lower() == value.strip().lower():
        raise ValueError(f"Không nhận ra viết tắt: {value!r}")
    return result

