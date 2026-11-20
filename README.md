# Màn hình biết ngón tay bạn ở đâu bằng cách nào?

Video hoàn chỉnh: **44.2 giây · 1080×1920 · 9:16 · 30fps · H.264/AAC**.

- [Man_Hinh_Cam_Ung_44_2s_1080x1920.mp4](Man_Hinh_Cam_Ung_44_2s_1080x1920.mp4) — xem/tải MP4.
- [Gói đầy đủ](Man_Hinh_Cam_Ung_DOWNLOAD.zip).
- [Phụ đề tiếng Việt](Man_Hinh_Cam_Ung.vi.srt).
- [Báo cáo thực tế](Production_Report.md).

Giữ nguyên 221 tiếng theo cách đếm khoảng trắng của kịch bản. Nhịp khoảng5tiếng/giây, có chuyển động tay/nhân vật, điện cực và tín hiệu, kéo ảnh, cuộn trang, phóng to hai điểm, nhạc và 37 SFX. Không phải slideshow ảnh.

**Đây là sơ đồ cảm ứng điện dung phổ biến được giản lược**, không đại diện mọi công nghệ màn hình. Găng tay thường có thể không hoạt động; găng tay cảm ứng có thể hoạt động. Thanh tín hiệu không phải số đo thực. Không tuyên bố mọi màn hình đều không có cảm biến lực.

Giọng: adapter Minh Quân, preset thực tế Hải Đăng, nam Bắc tự nhiên; VieNeu-TTS v3 Turbo, ONNX CPU ngoại tuyến. Không có API trả phí hoặc trọng số trong gói.

Xem bằng trình duyệt/VLC. Để dùng trang preview sau khi giải nén: tạo thư mục `output`, chép MP4/SRT và `index.html` từ gốc ZIP vào `output`, chạy `python production/serve.py` rồi mở http://127.0.0.1:8833/.

Tái dựng trong môi trường Video Shotcraft: Python với NumPy/Pillow, Node.js với @napi-rs/canvas, FFmpeg. Renderer tìm canvas tại `/workspace/video-shotcraft/workbench/package.json`; đổi đường dẫn nếu môi trường khác. Giữ các thư mục audio/assets/manifests/production/qa/logs/output cạnh nhau. Metadata TTS gốc đã kèm nên không cần chạy lại model.

```bash
mkdir -p output qa logs
python production/prepare.py
python production/audio.py
node production/film.mjs --preflight
node production/film.mjs --full
python production/finish.py
python production/report.py
```

File WAV gốc được bảo toàn. Xem CREDITS.md và Production_Report.md.
