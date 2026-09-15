"""Chuẩn hoá cách viết tiền thường gặp tại Việt Nam."""

from decimal import Decimal
import re

from .numbers import read_integer

_MULTIPLIERS = {
    "k": 1_000,
    "nghìn": 1_000,
    "ngàn": 1_000,
    "tr": 1_000_000,
    "triệu": 1_000_000,
    "tỷ": 1_000_000_000,
}

_CURRENCY_RE = re.compile(
    r"(?<!\w)(?P<num>\d+(?:[.,]\d+)*)\s*(?P<unit>nghìn|ngàn|triệu|tỷ|tr|k|₫|đ|vnd)(?!\w)"
    r"(?:\s*đồng)?",
    re.IGNORECASE,
)


def _amount(raw: str, unit: str) -> int:
    unit = unit.lower()
    if unit in {"đ", "₫", "vnd"}:
        # Với đồng, dấu phân nhóm ba chữ số không phải phần thập phân.
        number = raw.replace(".", "").replace(",", "")
        return int(number)
    normalized = raw.replace(".", ",")
    if normalized.count(",") > 1:
        normalized = normalized.replace(",", "")
    value = Decimal(normalized.replace(",", "."))
    return int(value * _MULTIPLIERS[unit])


def read_currency(value: str) -> str:
    match = _CURRENCY_RE.fullmatch(value.strip())
    if not match:
        raise ValueError(f"Tiền tệ không hợp lệ: {value!r}")
    return f"{read_integer(_amount(match['num'], match['unit']))} đồng"


def normalize_currency(text: str) -> str:
    return _CURRENCY_RE.sub(lambda match: read_currency(match.group()), text)
