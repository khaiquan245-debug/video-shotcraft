# Kết quả thực tế — Điện thoại gọi về quá khứ

Tệp MP4 thật dài **34.000 giây**, **1080×1920**, **30 fps**, **1020 frame**, có H.264 yuv420p và AAC stereo 48 kHz. Giữ nguyên 170 tiếng theo khoảng trắng và toàn bộ thứ tự lời kể người dùng. Đây là hoạt hình vector 2D có khớp tay/chân, động tác cầm/bấm điện thoại, cốc cà phê, chuyển đồ vật và chạy; không phải slideshow ảnh tĩnh.

## Nhịp kể và dừng

| Chỉ số | Video mẫu | Phim mới |
|---|---|---|
| Thời lượng | 38,22 giây | 34 giây |
| Tiếng tách theo khoảng trắng | 191, lời dựng lại | 170, nguyên văn |
| Mật độ lời toàn phim | ≈5,00/giây | 5,00/giây |

Video vừa tải được xác nhận trùng mẫu đã phân tích bằng SHA-256. Mốc ASR của mẫu không đồng nhất với phép đo RMS trên track giọng riêng; không tuyên bố mọi khoảng nghỉ giống hệt hay cùng giọng/model với mẫu.

Giọng native 39.9 giây được giữ file gốc. Thu gọn biên câu với đệm 40/45 ms và khoảng nối 45 ms, riêng trước câu cảnh báo cuối là 150 ms trước tempo. Bản ghép 35.060 giây được xử lý FFmpeg atempo=1.043452, giữ cao độ, cho giọng 33.608 giây. Không xóa hoặc thêm từ. Khoảng yên lớn nhất giữa phần có lời theo RMS<0,003 là **0.33 giây**; quanh lần đổi sang câu cảnh báo đo được khoảng **0.17 giây**. Đây là phép đo trên stem giọng trước master mix.

## Hình, đạo cụ và âm thanh

Nhân vật ở hiện tại/quá khứ/tương lai dùng cùng hình và rig; vai tương lai thêm tóc xám, người bán có áo/mũ/râu riêng. Khung hiện tại/quá khứ giúp đọc hệ quả của lời nhắc. Điện thoại giữ cùng hình, luôn bám cổ tay khi được cầm; không nhân đôi cùng một chiếc trên quầy và trong tay sau khi nhặt. Cốc đặt trên bàn sau khi máy tính hồi phục; hộp giày biến mất và không xuất hiện lại khi biệt thự hình thành. Cảnh chạy có chu kỳ chân và quay đầu; cuối phim ngón tay dừng trước phím gọi.

Biến đổi diễn ra bằng thay đổi trạng thái vật thể/nền vẽ và động tác, không dựa vào cập nhật chữ. Đã sửa cao độ quầy/mặt sàn, chân ghế biệt thự, giữ cốc cà phê, chuyển điện thoại từ bàn tay lên tai, và tránh vẽ ngón tay bấm điện thoại khi tay đang cầm cốc. Những kiểm tra rig không chứng minh mọi che khuất hoặc chuyển động đều hoàn hảo.

Giọng thực tế **VieNeu-TTS v3 Turbo**, **ONNX CPU offline**, **Hải Đăng** (alias **Minh Quân**). Câu cảnh báo dùng cùng voice qua highpass/lowpass/EQ kiểu điện thoại; không tạo giọng mới hoặc thêm thoại. Nhạc và 36 sự kiện SFX tự tổng hợp; nhạc chuông nguyên tác, nhạc nền nhường chỗ cho cuộc gọi cuối. 47 cụm phụ đề một dòng, theo biên câu đã đo và biên cụm nghĩa ước lượng; chưa forced alignment từng từ.

## QA

- Giải mã toàn bộ MP4 thành công; âm lượng **-14.1 LUFS**, true peak **-1.8 dBTP**.
- Khoảng yên lớn nhất trên toàn track giọng: **0.36 giây**, gồm đuôi kết.
- Rig solver kiểm tra **6864 mẫu**, **0 đích ngoài tầm**; sai số chiều dài xương tối đa **4.97e-14**.
- SHA-256: `955e59cb587aaf408575169c7774ed428be5151f57ef5e390684c4f324978e0e`.

Đã xem ảnh trích từ MP4 thật ở các nhịp chính, kiểm tra browser playback 1× để xác nhận tệp chạy hết. Phiên kiểm tra phát tắt tiếng, không thay cho người dùng nghe đánh giá chất giọng/nhạc/SFX. Không tự chứng nhận tương đương thẩm mỹ với mẫu hoặc sự duyệt của người dùng.

Các dự án cũ, narration đã có và installed skills được giữ nguyên. Model weights nằm ngoài Git. Toàn bộ TTS/render/mix chạy local, không paid API. Dự án: `/workspace/outputs/phone-to-past-20261120`.
