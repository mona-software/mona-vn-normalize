"""Đọc số thành chữ tiếng Việt."""

from decimal import Decimal, InvalidOperation
import re
from typing import Union

DIGITS = ("không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín")
SCALES = ("", "nghìn", "triệu", "tỷ", "nghìn tỷ", "triệu tỷ")


def _read_three(value: int, *, full: bool = False) -> str:
    hundreds, rest = divmod(value, 100)
    tens, ones = divmod(rest, 10)
    words = []
    if hundreds or full:
        words.extend((DIGITS[hundreds], "trăm"))
    if tens > 1:
        words.extend((DIGITS[tens], "mươi"))
        if ones == 1:
            words.append("mốt")
        elif ones == 4:
            words.append("tư")
        elif ones == 5:
            words.append("lăm")
        elif ones:
            words.append(DIGITS[ones])
    elif tens == 1:
        words.append("mười")
        if ones == 5:
            words.append("lăm")
        elif ones:
            words.append(DIGITS[ones])
    elif ones:
        if hundreds or full:
            words.append("lẻ")
        words.append(DIGITS[ones])
    return " ".join(words)


def read_integer(value: int) -> str:
    """Đọc số nguyên, hỗ trợ số âm và các số nhỏ hơn 10^18."""
    if value == 0:
        return DIGITS[0]
    if value < 0:
        return "âm " + read_integer(-value)
    groups = []
    while value:
        groups.append(value % 1000)
        value //= 1000
    if len(groups) > len(SCALES):
        raise ValueError("Số quá lớn để đọc")
    parts = []
    highest = len(groups) - 1
    for index in range(highest, -1, -1):
        group = groups[index]
        if not group:
            continue
        # Nhóm cuối phải đọc đủ hàng trăm khi phía trước còn nhóm lớn hơn.
        full = index == 0 and highest > 0 and group < 100
        words = _read_three(group, full=full)
        scale = SCALES[index]
        parts.append(f"{words} {scale}".strip())
    return " ".join(parts)


def read_number(value: Union[int, float, Decimal, str]) -> str:
    """Đọc số nguyên hoặc thập phân; phần sau dấu phẩy được đọc từng chữ số."""
    if isinstance(value, bool):
        raise TypeError("Giá trị boolean không phải là số hợp lệ")
    raw = str(value).strip()
    raw = raw.replace(" ", "")
    if not raw:
        raise ValueError("Số không được để trống")
    sign = ""
    if raw.startswith(("-", "+")):
        sign, raw = raw[0], raw[1:]
    # Dấu chấm theo nhóm ba chữ số là phân cách hàng nghìn kiểu Việt Nam.
    if re.fullmatch(r"\d{1,3}(?:\.\d{3})+", raw):
        raw = raw.replace(".", "")
    elif "," in raw and "." in raw:
        raw = raw.replace(".", "").replace(",", ".")
    else:
        raw = raw.replace(",", ".")
    if not re.fullmatch(r"\d+(?:\.\d+)?", raw):
        raise ValueError(f"Số không hợp lệ: {value!r}")
    integer, dot, fraction = raw.partition(".")
    result = read_integer(int(integer))
    if dot:
        result += " phẩy " + " ".join(DIGITS[int(char)] for char in fraction)
    if sign == "-":
        result = "âm " + result
    return result


_NUMBER_RE = re.compile(r"(?<![\w])[-+]?\d+(?:[.,]\d+)*(?![\w])", re.UNICODE)


def normalize_numbers(text: str) -> str:
    return _NUMBER_RE.sub(lambda match: read_number(match.group()), text)

