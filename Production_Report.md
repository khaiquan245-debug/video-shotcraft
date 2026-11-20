# Kết quả sản xuất thực tế

**Biến một thân cây rỗng thành ngôi nhà — 30 giây, 9:16.** Lời kể giữ nguyên 149 tiếng tách theo khoảng trắng, đạt 4.97 tiếng/giây trên toàn phim. Đây là cách đếm gần đúng theo khoảng trắng tiếng Việt, không phải đo âm tiết ngữ âm hoặc điểm chất lượng.

Phim thật có hình và tiếng, 1080×1920, 30 fps, 900 frame. Nhân vật, dụng cụ, đồ vật và góc máy chuyển động; không dựng từ slideshow ảnh tĩnh.

## Diễn hoạt và bố cục

Các khối kể: tìm cây → đặt rìu xuống → quét dọn gỗ mục → cưa rộng cửa → phòng tối → tạo hai cửa sổ → lát sàn → dựng giường → nóng/ngột ngạt → đục khe trên cao → lắp bản lề/cửa → đặt chậu cây/bật đèn → mở cửa và giới thiệu ngôi nhà.

Dùng nhiều góc cận theo tay và dụng cụ, hai góc cửa sổ nối bằng cut, khung cao cho công việc thông gió, mặt cắt cho nội thất và góc kéo rộng khi hoàn thiện. Mặt cắt là quy ước minh họa: lớp vỏ phía trước và khúc gỗ đặt rìu ở ngoài được bỏ khi nhìn phòng; đây không phải sự biến mất của đồ vật trong cốt truyện.

Đã sửa trong nháp: đặt rìu lệch khỏi mặt; đưa nhân vật ra khỏi vùng khúc gỗ khi lắp bản lề; điều chỉnh tư thế và tay cầm búa theo bản lề trên/dưới; đưa khúc gỗ ra khỏi lớp nhìn nội thất; chỉnh tay/chậu cây/mặt bàn; đặt chân lên mặt giàn công tác; chuyển bước trên giàn và qua cửa theo nhịp chân. Dụng cụ bám theo cổ tay, không dùng cánh tay phụ.

## Giọng và âm thanh

Model thực tế: **VieNeu-TTS v3 Turbo**, **ONNX CPU offline**. Giọng thực tế **Hải Đăng**; **Minh Quân** là alias trong adapter. Native 33.9 giây được bảo toàn; biên câu giữ đệm 40/45 ms, nối 45 ms; bản ghép 30.265 giây, FFmpeg atempo=1.024196, giữ cao độ, thành 29.549 giây. Không cắt/thêm lời, không ghi đè narration của dự án cũ.

43 cụm phụ đề một dòng; mốc câu theo đoạn TTS đã đo, biên cụm trong câu ước lượng, chưa forced alignment từng từ. 57 sự kiện Foley có vật thể/va chạm/địa điểm trong spotting list; nhạc pluck tự sáng tác và ambience rừng tự tổng hợp, phối ưu tiên giọng.

## Kiểm tra tệp đã render

- MP4 30.000 giây, H.264 yuv420p/AAC stereo 48 kHz; giải mã toàn bộ thành công.
- Âm lượng -14.3 LUFS, true peak -2.0 dBTP.
- Khoảng yên dài nhất trên track giọng RMS<0,003: 0.42 giây; phần giữa các đoạn có lời:0.29 giây.
- Rig: 3600 mẫu tay/chân, 0 đích ngoài tầm; sai số chiều dài xương tối đa 4.97e-14.
- SHA-256:`b7c3a514aeeab9a5690fada53e32ef15cd8dfd843b68d29988941aa44f9411aa`; dung lượng 7332313 bytes.

Xem ảnh trích từ MP4 thật ở các nhịp công cụ và các chuyển cảnh; phát thử trình duyệt 1× để kiểm tra kỹ thuật. Phiên phát kiểm tra tắt tiếng; chưa có duyệt phát âm/độ dễ nghe bằng tai người. Các số đo không bảo đảm mọi che khuất hoặc diễn xuất đều hoàn hảo, không tự chứng nhận tương đương thẩm mỹ với mẫu hay sự duyệt của người dùng.

Bản phim cũ và installed skills không bị sửa. Model weights ở ngoài Git. Không dùng paid API, cloud inference hay subscription mới. Dự án mới: `/workspace/outputs/hollow-tree-home-20261120`.
