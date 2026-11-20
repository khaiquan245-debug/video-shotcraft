# Tô ngũ cốc — FAST V2

Mở `Ngu_Coc_FAST_V2_31_2s_1080x1920.mp4`:31,2 giây, 1080×1920, 30 fps, có lời kể tiếng Việt, phụ đề, nhạc và SFX.

Giữ nguyên 154 tiếng của kịch bản và toàn bộ tạo hình. Mục tiêu nhịp theo mẫu người dùng: gần 5 tiếng/giây, hành động nối tiếp, không kéo dài phim để đủ 40 giây. Bản cũ40 giây vẫn nguyên vẹn.

Giọng gốc VieNeu-TTS v3 Turbo, CPU ONNX offline, Hải Đăng (adapter gọi bằng alias Minh Quân). Tái sử dụng WAV native đã có; thu gọn khoảng yên ở biên câu và khoảng nối, tăng tốc giọng khoảng 5,9% bằng FFmpeg atempo giữ cao độ. Không thu lại hoặc ghi đè giọng đã duyệt.

Hình được render lại ở 30 fps từ source với nhịp cảnh mới; camera, tiếp xúc và Foley theo cùng clock cảnh. Phụ đề theo clock audio. Không tăng tốc toàn bộ tệp MP4 cũ. Các chuyển động qua biên câu được nội suy theo khối hành động để tránh nhảy tư thế khi bỏ khoảng yên.

Xem `Comparison_Report.md`, `SHORTS_NHIP_KE_NHANH.md`, ảnh trích và QA trong ZIP. Chưa có duyệt bằng tai người; phụ đề trong câu dùng mốc cụm nghĩa ước lượng, không forced alignment từng từ. Không dùng API trả phí; model weights không nằm trong ZIP/Git.

Dựng lại trong Cloud hiện tại, với Canvas/FFmpeg đã cài:

```bash
python production/prepare_fast.py
python production/audio.py
node production/film.mjs --preflight
node production/film.mjs --full
python production/finish.py
python production/report.py
```

Cần runtime @napi-rs/canvas từ `/workspace/video-shotcraft/workbench/package.json`; các font và nguồn giọng đã có trong gói. Không chạy lại TTS vào WAV native đã có.
