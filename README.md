# mona-vn-normalize

A Python library that rewrites numbers, money, dates, times, phone numbers, units, abbreviations and Roman numerals in Vietnamese text as spelled-out Vietnamese words, for text-to-speech (TTS) and NLP pipelines.

The library targets Vietnamese text only. It was built while testing speech models for [MONA AI Lab](https://mona.media/ai-lab/).

## What it converts

| Group | Example input → output |
| --- | --- |
| Numbers | `1234` → *một nghìn hai trăm ba mươi tư* · `105` → *một trăm lẻ năm* |
| Money | `150.000đ` → *một trăm năm mươi nghìn đồng* · `2tr` → *hai triệu đồng* · `1,5 triệu` → *một triệu năm trăm nghìn đồng* |
| Dates | `15/09/2026` → *ngày mười lăm tháng chín năm hai nghìn không trăm hai mươi sáu* |
| Times | `14:30` → *mười bốn giờ ba mươi phút* · `9h` → *chín giờ* |
| Phone numbers | `1900 636 648` → *một chín không không sáu ba sáu sáu bốn tám* |
| Abbreviations | `Tp.HCM` → *thành phố Hồ Chí Minh* · `TNHH` → *trách nhiệm hữu hạn* |
| Units | `25°C` → *hai mươi lăm độ C* · `50%` → *năm mươi phần trăm* · `10km` → *mười ki lô mét* |
| Roman numerals | `thế kỷ XXI` → *thế kỷ hai mươi mốt* |

## Install

Requires Python 3.9+. Standard library only.

```bash
git clone https://github.com/mona-software/mona-vn-normalize
cd mona-vn-normalize
pip install -e .
```

## Quick start

```bash
python examples/demo.py
```

```python
from mona_vn_normalize import normalize

normalize("Hẹn lúc 14:30 ngày 15/09/2026 tại Tp.HCM, giá 150.000đ.")
# → "Hẹn lúc mười bốn giờ ba mươi phút ngày mười lăm tháng chín năm hai nghìn
#    không trăm hai mươi sáu tại thành phố Hồ Chí Minh, giá một trăm năm mươi nghìn đồng."
```

## Usage

`normalize(text, *, currency=True, phone=True, dates=True, times=True, numbers=True, units=True, abbrev=True, roman=True)` runs the converters in a fixed order (currency, phone, dates, times, abbreviations, Roman numerals, units, then plain numbers) so overlapping tokens are handled before generic number reading. Turn any group off with its keyword:

```python
normalize(text, phone=False, roman=False)
```

Single-value helpers are also exported: `read_number`, `read_integer`, `read_currency`, `read_date`, `read_time`, `read_phone`, `read_abbreviation`, `read_unit`, `read_roman`, `roman_to_int` and `clean_text`.

## Development

```bash
pip install -e ".[dev]"
pytest -q
```

Tests run offline; all test inputs are hand-written examples.

## License

MIT, see [LICENSE](LICENSE).

**`mona-vn-normalize` is a product of MONA Software, a member of The MONA Group.**
