# Biến một thân cây rỗng thành ngôi nhà

Video 30 giây, 1080×1920, 30 fps, hoạt hình 2D có nhân vật và đồ vật chuyển động. Mở `Than_Cay_Rong_Thanh_Ngoi_Nha_30s_1080x1920.mp4` hoặc `index.html`.

Giữ nguyên 149 tiếng của lời kể người dùng, gồm ngôi “anh ta”. Dựng theo nhịp Shorts đã chốt: gần 5 tiếng/giây, các thao tác nối nhau, kết gọn. Có phụ đề tiếng Việt, nhạc nguyên tác và SFX.

Giọng thực tế: VieNeu-TTS v3 Turbo chạy ONNX CPU offline, preset Hải Đăng; Minh Quân là alias của preset trong adapter hiện tại. File native dài 33,9 giây được giữ nguyên. Bản dựng thu gọn khoảng nghỉ và xử lý tốc độ khoảng 1,024×, giữ cao độ.

Phim dùng góc ngoài thân cây xen với mặt cắt minh họa nội thất. Khúc gỗ đặt rìu thuộc lớp ngoài, được ẩn khi nhìn mặt cắt bên trong. Các phần cửa, cửa sổ, sàn, giường và khe thông gió được giữ theo tiến độ câu chuyện.

ZIP có MP4, SRT, source Canvas/FFmpeg, các WAV, metadata giọng, font/giấy phép và QA. Không đóng gói model weights hoặc video tham khảo. Không API trả phí.

Muốn dựng lại, tạo bản sao dự án ở thư mục mới trước khi chạy; giữ các WAV đã duyệt. Source dùng @napi-rs/canvas đã cài tại `/workspace/video-shotcraft/workbench/package.json`:

```bash
python production/prepare.py
python production/audio.py
node production/film.mjs --preflight
node production/film.mjs --full
python production/finish.py
python production/report.py
```

Đọc `Production_Report.md` để xem kiểm tra thật và giới hạn. Mốc phụ đề trong câu được ước lượng theo cụm nghĩa, chưa forced-align từng từ. Kiểm tra kỹ thuật phát trình duyệt tắt tiếng không thay cho duyệt giọng bằng tai người.
