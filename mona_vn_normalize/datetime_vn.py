"""Chuẩn hoá ngày và giờ theo cách đọc tiếng Việt."""

import re
from .numbers import read_integer

_DATE_RE = re.compile(r"(?<!\d)(?P<day>\d{1,2})/(?P<month>\d{1,2})(?:/(?P<year>\d{2,4}))?(?!\d)")
_TIME_RE = re.compile(r"(?<!\d)(?P<hour>[01]?\d|2[0-3])(?:(?P<sep>:|h|g)(?P<minute>[0-5]\d)?)", re.IGNORECASE)


def read_date(value: str) -> str:
    match = _DATE_RE.fullmatch(value.strip())
    if not match:
        raise ValueError(f"Ngày không hợp lệ: {value!r}")
    day, month = int(match["day"]), int(match["month"])
    year = match["year"]
    if not 1 <= day <= 31 or not 1 <= month <= 12:
        raise ValueError(f"Ngày không hợp lệ: {value!r}")
    day_words = read_integer(day)
    if year is None and day <= 10:
        day_words = "mùng " + day_words
    result = f"ngày {day_words} tháng {read_integer(month)}"
    if year:
        full_year = int(year) + (2000 if len(year) == 2 else 0)
        result += f" năm {read_integer(full_year)}"
    return result


def read_time(value: str) -> str:
    match = _TIME_RE.fullmatch(value.strip())
    if not match:
        raise ValueError(f"Giờ không hợp lệ: {value!r}")
    result = f"{read_integer(int(match['hour']))} giờ"
    if match["minute"] is not None:
        result += f" {read_integer(int(match['minute']))} phút"
    return result


def normalize_dates(text: str) -> str:
    # Nuốt luôn từ "ngày" nếu người viết đã đặt trước token để không lặp từ.
    pattern = re.compile(r"(?:\bngày\s+)?" + _DATE_RE.pattern, re.IGNORECASE)
    return pattern.sub(
        lambda match: read_date(
            f"{match['day']}/{match['month']}" + (f"/{match['year']}" if match['year'] else "")
        ),
        text,
    )


def normalize_times(text: str) -> str:
    return _TIME_RE.sub(lambda match: read_time(match.group()), text)
