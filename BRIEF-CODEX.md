# BRIEF — build repo `mona-vn-normalize` (Python)

Bạn là kỹ sư. Dựng 1 thư viện Python **chạy thật, có test pass** trong ĐÚNG thư mục hiện tại (`--cd`). KHÔNG hỏi lại, KHÔNG chờ. Làm xong in tóm tắt + kết quả `pytest`.

## Mục tiêu
`mona-vn-normalize` = thư viện **chuẩn hoá văn bản tiếng Việt trước khi đưa vào TTS / NLP**. Biến các token khó đọc (số, tiền, ngày giờ, số điện thoại, viết tắt, ký hiệu, đơn vị) thành **chữ đọc được đúng tiếng Việt có dấu**, để engine đọc giọng không vấp. Đây là công cụ mở tách ra từ việc MONA test model giọng nói (Muse Voice) — phải hữu ích thật.

## Kiến trúc (stdlib thuần, KHÔNG deps runtime nặng)
```
mona_vn_normalize/
  __init__.py         # export normalize() + các hàm con
  numbers.py          # số -> chữ (nguyên, thập phân, âm)
  currency.py         # tiền: 150.000đ, 1,5 triệu, 2tr, 500k, 1 tỷ -> "... đồng"
  datetime_vn.py      # ngày 15/09/2026, 2/9 ; giờ 14:30, 9h30, 9g30
  phone.py            # SĐT: 0909 636 648, 1900 636 648, +84... -> đọc từng số
  abbrev.py           # viết tắt: Tp.HCM, Q.1, P., đ/c, TS., ThS., CLB, TNHH...
  units.py            # %, °C, km, kg, m2, m³, +, -, =, /, ~ ...
  roman.py            # số La Mã theo ngữ cảnh: thế kỷ XXI, khoá VII
  text.py             # dọn khoảng trắng/dấu câu, giữ nguyên dấu tiếng Việt
tests/                # pytest, >= 28 test, phủ từng nhóm bằng ví dụ VN thật
pyproject.toml        # setuptools, python>=3.9, name=mona-vn-normalize, KHÔNG deps runtime; [dev] = pytest
.gitignore            # __pycache__, .venv, *.egg-info, dist
examples/demo.py      # in trước/sau vài câu mẫu
```

## API
- `normalize(text: str, *, currency=True, phone=True, dates=True, times=True, numbers=True, units=True, abbrev=True, roman=True) -> str`
  chạy pipeline theo thứ tự an toàn (currency/phone/date/time TRƯỚC number thuần để không nuốt nhau).
- Mỗi module có hàm riêng test được, vd `read_number(1234) -> "một nghìn hai trăm ba mươi tư"`, `read_currency("150.000đ") -> "một trăm năm mươi nghìn đồng"`.

## Yêu cầu ĐÚNG tiếng Việt (test khoá cứng các case này)
- Số: 1→"một", 15→"mười lăm", 21→"hai mươi mốt", 24→"hai mươi tư" (hoặc "bốn", chọn "tư" cho hàng đơn vị sau chục ≥2), 100→"một trăm", 105→"một trăm lẻ năm", 1000→"một nghìn", 1234→"một nghìn hai trăm ba mươi tư", 1000000→"một triệu", 1500000→"một triệu năm trăm nghìn".
- Tiền: "500k"→"năm trăm nghìn đồng", "2tr"→"hai triệu đồng", "1,5 triệu"→"một triệu năm trăm nghìn đồng", "150.000đ"→"một trăm năm mươi nghìn đồng", "1 tỷ"→"một tỷ đồng".
- Ngày: "15/09/2026"→"ngày mười lăm tháng chín năm hai nghìn không trăm hai mươi sáu"; "2/9"→"ngày mùng hai tháng chín" (mùng cho ngày 1-10 khi không có năm; nếu có năm dùng "ngày hai").
- Giờ: "14:30"→"mười bốn giờ ba mươi phút"; "9h30"→"chín giờ ba mươi phút"; "9h"→"chín giờ".
- SĐT: "1900 636 648"→"một chín không không sáu ba sáu sáu bốn tám"; "0909636648" đọc từng chữ số (0→"không").
- Viết tắt: "Tp.HCM"→"thành phố Hồ Chí Minh"; "Q.1"→"quận một"; "TNHH"→"trách nhiệm hữu hạn"; "CLB"→"câu lạc bộ".
- Đơn vị: "25°C"→"hai mươi lăm độ C"; "50%"→"năm mươi phần trăm"; "10km"→"mười ki lô mét"; "5kg"→"năm ki lô gam".
- La Mã: "thế kỷ XXI"→"thế kỷ hai mươi mốt"; "khoá VII"→"khoá bảy". (chỉ đổi khi đứng sau từ khoá gợi ngữ cảnh: thế kỷ/khoá/quý/chương/kỳ...)
- GIỮ NGUYÊN dấu tiếng Việt, KHÔNG bẻ chữ. Không đổi các từ đã là chữ thường.

## Ràng buộc
- ⛔️ KHÔNG lộ endpoint/key nội bộ, KHÔNG gọi mạng, KHÔNG dữ liệu khách thật — toàn bộ ví dụ tự soạn.
- Code sạch, comment tiếng Việt chỗ logic khó (số→chữ). Ít magic.
- README để TRỐNG/placeholder 1 dòng — **Claude sẽ tự viết README + LICENSE**, bạn KHÔNG cần lo phần đó.
- Chạy `pytest -q` phải PASS hết (>=28 test). In kết quả pytest ở cuối.
```
