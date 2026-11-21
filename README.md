# Cục tẩy xóa mọi thứ

MP4 hoàn chỉnh 50,4 giây, 1080×1920, 30 fps, có narration tiếng Việt, phụ đề, SFX và nhạc gốc. Mở `Cuc_Tay_Xoa_Moi_Thu_50_4s_1080x1920.mp4` hoặc `index.html`.

Giữ nguyên kịch bản 252 tiếng theo khoảng trắng, nhịp toàn phim 5 tiếng/giây theo mẫu “Biến đống rơm thành căn cứ”. Camera theo hành động, cục tẩy lăn xuống dốc, chụp lại, rơi xuống hố và leo ra. Có chuyển động nhân vật/đồ vật và trạng thái bối cảnh liên tục.

Voice thực tế: VieNeu-TTS v3 Turbo, ONNX CPU offline, preset Hải Đăng (alias Minh Quân trong adapter). WAV native được giữ nguyên. Bản dựng thu gọn khoảng yên và dùng atempo 1,0786× giữ cao độ.

ZIP có MP4, SRT, WAV native/đã dựng, stem mix/nhạc/SFX, source Canvas/FFmpeg, font/giấy phép, timeline và QA. Không kèm trọng số model hoặc video/audio tham khảo. Không API trả phí.

Dựng lại trong bản sao thư mục mới để giữ bản đã duyệt. Môi trường hiện tại cần `@napi-rs/canvas` qua `/workspace/video-shotcraft/workbench/package.json`, FFmpeg, Python với NumPy/Pillow. Nếu chuyển máy, sửa đường dẫn createRequire sang nơi cài Canvas của bạn; không cần model TTS để render lại từ WAV kèm ZIP.

```bash
python production/prepare.py
python production/audio.py
node production/film.mjs --preflight
node production/film.mjs --full
python production/finish.py
python production/report.py
python production/serve.py
```

Preview local: http://127.0.0.1:8839/ . Mở MP4 tải về bằng trình phát video thông thường cũng được. Biên phụ đề theo cụm nghĩa trong câu đã đo, chưa forced-align từng từ. Phạm vi QA và giới hạn nghe/xem ghi trong Production_Report.md.
