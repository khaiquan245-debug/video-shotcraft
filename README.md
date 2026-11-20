# Điều gì xảy ra bên trong máy ATM?

Video hoàn chỉnh: **38.2 giây · 1080×1920 · 9:16 · 30fps · H.264/AAC**.

- [Ben_Trong_May_ATM_38_2s_1080x1920.mp4](Ben_Trong_May_ATM_38_2s_1080x1920.mp4) — mở để xem hoặc tải.
- [Gói video, phụ đề và mã nguồn](Ben_Trong_May_ATM_DOWNLOAD.zip).
- [Phụ đề tiếng Việt](Ben_Trong_May_ATM.vi.srt).
- [Báo cáo thực tế](Production_Report.md).

Giữ nguyên toàn bộ lời kể người dùng: 191 tiếng theo cách đếm khoảng trắng. Nhịp khoảng 5 tiếng/giây. Có hoạt hình nhân vật và cơ cấu nhả tiền, nhạc nền, SFX và phụ đề cháy vào hình.

**Hình cắt lớp là mô hình minh họa giản lược. Cấu tạo máy, thứ tự trả thẻ/tiền và quy trình xử lý lỗi có thể khác nhau.** Minh họa giao dịch bằng 5 tờ 200.000đ; ví dụ một tờ không phù hợp được tách riêng và thay bằng tờ hợp lệ, không tính thêm vào số tiền trao ra.

Giọng yêu cầu trong adapter: Minh Quân. Preset thực tế: Hải Đăng, nam Bắc tự nhiên; model VieNeu-TTS v3 Turbo, ONNX CPU ngoại tuyến. Không dùng API trả phí. Trọng số không có trong Git hoặc ZIP.

Mở MP4 bằng trình duyệt/VLC, hoặc chạy `python production/serve.py` sau khi giải nén rồi mở http://127.0.0.1:8831/.

Tái dựng trong môi trường Video Shotcraft đã cài: Python + NumPy + Pillow, Node.js + @napi-rs/canvas, FFmpeg. Bộ mã hiện tìm canvas trong `/workspace/video-shotcraft/workbench/package.json`; sửa đường dẫn này nếu vị trí cài đặt khác. Giữ thư mục `audio`, `assets`, `manifests`, `production`, `qa`, `logs`, `output` trong cùng gốc. WAV gốc được lưu nguyên, không cần chạy lại TTS.

```bash
mkdir -p output qa logs
python production/prepare.py
python production/audio.py
node production/film.mjs --preflight
node production/film.mjs --full
python production/finish.py
python production/report.py
```

Trước khi chạy, chép MP4/SRT và các tài liệu ở gốc ZIP vào `output/` nếu muốn dùng trang preview. Xem CREDITS.md cho nguồn và giấy phép.
