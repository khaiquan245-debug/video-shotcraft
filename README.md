# Chiếc điện thoại gọi về quá khứ

Video 34 giây, 1080×1920, 30 fps, hoạt hình 2D có nhân vật và đồ vật chuyển động. Mở `Dien_Thoai_Goi_Ve_Qua_Khu_34s_1080x1920.mp4` hoặc `index.html`.

Giữ nguyên 170 tiếng của kịch bản; nhịp toàn phim 5 tiếng/giây theo mẫu người dùng. Có phụ đề tiếng Việt, nhạc và SFX. Nhịp trước câu cảnh báo cuối ngắn, không thêm khoảng đứng hình dài.

Giọng thực tế: VieNeu-TTS v3 Turbo, ONNX CPU offline, preset Hải Đăng; Minh Quân là alias trong adapter hiện tại. Giọng native được giữ nguyên; bản dựng chỉ thu gọn khoảng yên và xử lý tốc độ khoảng 1,043×, giữ cao độ. Câu cuối dùng cùng giọng qua EQ điện thoại, không đổi model hoặc recast người kể.

Các khung hiện tại/quá khứ dùng cùng nhân vật với bối cảnh và hành động tương ứng. Điện thoại cũ giữ nguyên thiết kế qua toàn phim. Máy tính được sửa tại chỗ, hộp giày không trở lại sau khi biến mất, và căn phòng đổi quanh nhân vật thành biệt thự. Cuối phim nhân vật chưa bấm cuộc gọi tiếp theo.

ZIP có MP4, SRT, source Canvas/FFmpeg, các WAV, metadata, font/giấy phép và QA; không có model weights hoặc video tham khảo. Không API trả phí.

Muốn dựng lại, tạo bản sao ở thư mục mới và giữ các WAV đã duyệt. Cần Canvas hiện có trong `/workspace/video-shotcraft/workbench/package.json`:

```bash
python production/prepare.py
python production/audio.py
node production/film.mjs --preflight
node production/film.mjs --full
python production/finish.py
python production/report.py
```

Đọc `Production_Report.md` để xem kiểm tra và giới hạn. Biên phụ đề trong câu ước lượng theo cụm nghĩa, chưa forced-align từng từ; không tự nhận đã duyệt phát âm bằng tai người.
