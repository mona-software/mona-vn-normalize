"""Dọn khoảng trắng và dấu câu mà không làm mất dấu tiếng Việt."""

import re


def clean_text(text: str) -> str:
    text = re.sub(r"[\t\r\n]+", " ", text)
    text = re.sub(r" {2,}", " ", text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r"([,;:!?])(?=\S)", r"\1 ", text)
    return text.strip()

