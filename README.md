# mona-vn-normalize

**Chuẩn hoá tiếng Việt trước khi đưa vào giọng nói (TTS) hoặc xử lý ngôn ngữ.**
*Vietnamese text normalizer for TTS/NLP — turns numbers, money, dates, phone numbers and abbreviations into properly spelled Vietnamese words.*

Đây là bộ đồ nghề MONA tách ra từ chuyên mục [MONA AI Lab](https://mona.media/ai-lab/) khi tụi em test mấy model giọng nói. Máy đọc tiếng Việt hay vấp đúng ở chỗ số, tiền, ngày giờ, số điện thoại, viết tắt — thư viện này biến chúng thành chữ đọc được, đúng dấu, để engine TTS không đọc sai.

## Vì sao có bộ này

Model TTS mới bây giờ đọc tiếng Việt khá tự nhiên, nhưng đưa `150.000đ`, `14:30`, `0909 636 648`, `Tp.HCM` vào là nó lúng túng ngay: đọc thiếu số, đọc sai đơn vị, hoặc bỏ luôn. Khách nghe tổng đài đọc "một trăm năm mươi nghìn đồng" khác hẳn nghe "một năm không không không đ". Việc chuẩn hoá phần chữ TRƯỚC khi đẩy vào TTS là khâu quyết định chất lượng, mà lại ít ai làm tử tế cho tiếng Việt. Tụi em làm, rồi mở ra.

## Nó làm được gì

| Nhóm | Ví dụ |
|---|---|
| Số | `1234` → *một nghìn hai trăm ba mươi tư* · `105` → *một trăm lẻ năm* |
| Tiền | `150.000đ` → *một trăm năm mươi nghìn đồng* · `2tr` → *hai triệu đồng* · `1,5 triệu` → *một triệu năm trăm nghìn đồng* |
| Ngày | `15/09/2026` → *ngày mười lăm tháng chín năm hai nghìn không trăm hai mươi sáu* |
| Giờ | `14:30` → *mười bốn giờ ba mươi phút* · `9h` → *chín giờ* |
| Số điện thoại | `1900 636 648` → *một chín không không sáu ba sáu sáu bốn tám* |
| Viết tắt | `Tp.HCM` → *thành phố Hồ Chí Minh* · `TNHH` → *trách nhiệm hữu hạn* |
| Đơn vị | `25°C` → *hai mươi lăm độ C* · `50%` → *năm mươi phần trăm* · `10km` → *mười ki lô mét* |
| Số La Mã | `thế kỷ XXI` → *thế kỷ hai mươi mốt* |

## Chạy thử

```bash
git clone https://github.com/themonagroup/mona-vn-normalize
cd mona-vn-normalize
python examples/demo.py
```

```python
from mona_vn_normalize import normalize

normalize("Hẹn lúc 14:30 ngày 15/09/2026 tại Tp.HCM, giá 150.000đ.")
# → "Hẹn lúc mười bốn giờ ba mươi phút ngày mười lăm tháng chín năm hai nghìn
#    không trăm hai mươi sáu tại thành phố Hồ Chí Minh, giá một trăm năm mươi nghìn đồng."
```

Bật/tắt từng nhóm nếu cần: `normalize(text, phone=False, roman=False)`. Mỗi nhóm cũng có hàm riêng gọi thẳng được: `read_number`, `read_currency`, `read_date`, `read_time`, `read_phone`, `read_abbreviation`, `read_unit`, `read_roman`.

## Cài như thư viện

```bash
pip install -e .          # dùng thẳng trong dự án
pytest -q                 # 59 test, chạy được offline, không cần API key
```

Chỉ dùng thư viện chuẩn của Python (>=3.9), không kéo dependency nặng.

## Dữ liệu

Toàn bộ ví dụ trong test là **tự soạn** — không có một dòng dữ liệu khách hàng thật nào. Anh chị đọc, sửa, thêm case thoải mái; gặp câu tiếng Việt nào máy đọc sai thì mở issue, tụi em thêm luật.

## Tuyên ngôn thị trường cùng tiến

MONA là một công ty phần mềm, chuyển đổi số, chuyển đổi AI, nhưng trên hết, MONA là một công ty dịch vụ B2B, là người hưởng lợi trực tiếp từ việc: **những doanh nghiệp Việt càng thành công, MONA càng có lợi**. Thị trường đi xuống, đi chậm, công nghệ yếu mới chính là điểm giết chết các cơ hội làm ăn trong tương lai của MONA. Nên, hơn ai hết, MONA mong muốn, và MONA thật sự can thiệp vào việc giúp đỡ anh chị thành công. Và chuyển đổi AI là chìa khóa cho sự thành công đó của chúng ta.

## Từ đâu ra

Từ [MONA AI Lab](https://mona.media/ai-lab/) — nơi MONA test model AI mới trên sản phẩm thật (tổng đài, chatbot, phần mềm) rồi báo cáo thẳng cái nào xài được. Xem thêm kho tài nguyên mở [MONA Open](https://mona.media/mona-open/), bộ công cụ [MONA GEO OS](https://mona.media/mona-geo-os/), và tác giả [Khánh Hùng — Founder The MONA](https://mona.media/profile/vy-nguyen-khanh-hung/).

Giấy phép: [MIT](LICENSE).
