"""Chuẩn hoá đơn vị đo lường và ký hiệu toán học."""

import re
from .numbers import read_number

_UNITS = {
    "°c": "độ C",
    "%": "phần trăm",
    "km": "ki lô mét",
    "kg": "ki lô gam",
    "m2": "mét vuông",
    "m²": "mét vuông",
    "m3": "mét khối",
    "m³": "mét khối",
    "cm": "xen ti mét",
    "mm": "mi li mét",
}
_UNIT_RE = re.compile(
    r"(?<![\w])(?P<num>\d+(?:[.,]\d+)?)\s*(?P<unit>°C|%|km|kg|cm|mm|m[23²³])(?!\w)",
    re.IGNORECASE,
)
_SYMBOLS = {"+": "cộng", "=": "bằng", "~": "xấp xỉ"}


def read_unit(value: str) -> str:
    match = _UNIT_RE.fullmatch(value.strip())
    if not match:
        raise ValueError(f"Đơn vị không hợp lệ: {value!r}")
    return f"{read_number(match['num'])} {_UNITS[match['unit'].lower()]}"


def normalize_units(text: str) -> str:
    text = _UNIT_RE.sub(lambda match: read_unit(match.group()), text)
    # Dấu trừ nằm giữa hai số là phép toán; dấu âm sát đầu số do numbers xử lý.
    text = re.sub(r"(?<=\d)\s*-\s*(?=\d)", " trừ ", text)
    for symbol, word in _SYMBOLS.items():
        text = re.sub(rf"\s*{re.escape(symbol)}\s*", f" {word} ", text)
    text = re.sub(r"\s/\s", " trên ", text)
    return text
