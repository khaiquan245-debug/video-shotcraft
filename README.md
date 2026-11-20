**Căn cứ gốc cây — bản mẫu 30 giây**

Mở `Can_Cu_Goc_Cay_30s_1080x1920.mp4` để xem phim đầy đủ. Phim có lời dẫn, phụ đề tiếng Việt, nhạc nền và hiệu ứng âm thanh.

Kịch bản mới: chui vào gốc cây tránh mưa → vá lỗ dột → nước tràn dưới chân → đào rãnh thoát nước → ếch theo rãnh vào → mắc võng lên cao → có căn cứ và dàn nhạc ếch.

- Hình: 1080×1920, dọc 9:16, 30 fps, 900 frame, 30.000 giây.
- Âm thanh: AAC stereo 48 kHz, -14.2 LUFS, peak -1.9 dBTP.
- Giọng: VieNeu-TTS v3 Turbo ONNX CPU offline. Preset yêu cầu “Minh Quân” ánh xạ tới “Hải Đăng” trong bộ cài. Giữ tốc độ native 1.0; không dùng API trả phí.
- WAV nguồn dài 22,96 giây được giữ nguyên; timeline 30 giây có thêm các khoảng hành động/SFX. Khoảng yên dài nhất trong giọng theo ngưỡng RMS: 2.86s.
- Hình vẽ gốc và nhân vật được vẽ/diễn hoạt bằng vector local; không chèn frame của video tham chiếu, không dùng slideshow.

Đã kiểm tra: giải mã toàn bộ MP4; số frame/kích thước/fps; giới hạn đích IK của toàn bộ 900 frame; các ảnh trích từ video đã encode ở đoạn búa chạm gỗ, xẻng xuống đất, bước/nhảy lên võng; kiểm tra đọc phụ đề. Tệp `qa/final.json` ghi thông số thật. Lỗi phát hiện trong bản nháp và cách sửa lưu ở `qa/draft-findings.json`.

Giới hạn: hoạt hình 2D và bàn tay được giản lược; không tự chứng nhận ngang chất lượng bản tham chiếu. Phụ đề chia theo cụm nghĩa trong khoảng audio từng câu, chưa phải forced alignment từng từ. Chưa thẩm định cảm xúc giọng/nhạc/SFX bằng tai người; phát trình duyệt tắt tiếng chỉ là kiểm tra tệp chơi được.

Dự án gốc tại `/workspace/outputs/tree-hollow-30s-20261120/`. Phim và các dự án Video Shotcraft trước đó không bị thay thế.
