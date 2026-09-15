from pathlib import Path
import sys

# Cho phép chạy thẳng ``python examples/demo.py`` từ bản checkout.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mona_vn_normalize import normalize

samples = [
    "Hẹn lúc 14:30 ngày 15/09/2026 tại Tp.HCM.",
    "Giá 150.000đ, giảm 50% cho đơn từ 2tr.",
    "Gọi 0909 636 648, quãng đường 10km, nhiệt độ 25°C.",
]

for sample in samples:
    print("Trước:", sample)
    print("Sau:  ", normalize(sample))
    print()
