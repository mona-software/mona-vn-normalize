"""Nhận diện và đọc số điện thoại theo từng chữ số."""

import re
from .numbers import DIGITS

_PHONE_RE = re.compile(
    r"(?<!\d)(?:(?:\+84|0)(?:[ .-]*\d){8,10}"
    r"|1[ .-]*[89][ .-]*0[ .-]*0(?:[ .-]*\d){6})(?!\d)",
    re.IGNORECASE,
)


def read_phone(value: str) -> str:
    compact = re.sub(r"[ .()-]", "", value.strip())
    if compact.startswith("+84"):
        compact = "0" + compact[3:]
    if not compact.isdigit() or not 9 <= len(compact) <= 11:
        raise ValueError(f"Số điện thoại không hợp lệ: {value!r}")
    return " ".join(DIGITS[int(char)] for char in compact)


def normalize_phones(text: str) -> str:
    return _PHONE_RE.sub(lambda match: read_phone(match.group()), text)
