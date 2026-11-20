# Bạn tỉnh dậy trong tô ngũ cốc

Bản phim 40 giây, 1080×1920, 30 fps, hoạt hình 2D có chuyển động nhân vật và đồ vật. Giữ nguyên toàn bộ lời kể tiếng Việt được gửi trong cuộc trò chuyện. Không thêm câu thoại, không dùng API trả phí.

Mở `Ban_Tinh_Day_Trong_To_Ngu_Coc_40s_1080x1920.mp4` hoặc `index.html`. Nếu trình duyệt chỉ phát mà không tải, dùng tùy chọn tải của trình phát hoặc giải nén gói ZIP rồi mở MP4 bằng VLC/QuickTime.

Giọng: VieNeu-TTS v3 Turbo, ONNX CPU offline, preset Hải Đăng; adapter hiện tại dùng Minh Quân làm alias. Giọng native dài 37,6 giây, không tăng/giảm tốc, đặt tại 0,06 giây trên timeline. Hơn 2 giây cuối dành cho tiếng gõ và cú hé lộ.

Trong gói có MP4, phụ đề SRT, lời kể, shot manifest, source renderer/audio, font/giấy phép, WAV native và kết quả kiểm tra. Trọng số model không được đóng gói hoặc đưa vào Git. Các dự án cũ được giữ nguyên.

`Production_Report.md` nêu các kiểm tra thật và giới hạn. Source trong `production/` sử dụng các công cụ đã cài của Cloud hiện tại. Các lệnh dựng lại trong môi trường đó:

```bash
python production/prepare.py
python production/audio.py
node production/film.mjs --preflight
node production/film.mjs --full
python production/finish.py
```

Không chạy lại TTS vào đường dẫn WAV đã có. Adapter từ chối ghi đè; chọn tên mới nếu sau này đổi lời. Renderer dùng @napi-rs/canvas qua `/workspace/video-shotcraft/workbench/package.json`; model local và môi trường TTS nằm ngoài gói tải.
