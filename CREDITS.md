# Nguồn và công cụ

- Kịch bản, nhận xét và hai ảnh tham chiếu: người dùng cung cấp. Ảnh dùng hướng dẫn phong cách, không làm nền slideshow.
- Nhân vật, bối cảnh, diễn xuất và bố cục bản sửa: vector và rig khớp vẽ bằng mã local trong dự án này.
- Giọng kể: dùng nguyên bản WAV đã có, Minh Đức / VieNeu-TTS v3 Turbo ONNX CPU, model Apache-2.0. Không tổng hợp lại và không đổi giọng ở bản sửa này. Trọng số model không có trong gói tải hay Git.
- Nhạc nền và SFX: tổng hợp local bằng oscillator/noise trong `production/audio.py`; không lấy nhạc thương mại.
- Font Nunito: SIL Open Font License, kèm tệp OFL trong source.
- Công cụ: Python, NumPy, Pillow, Node.js, @napi-rs/canvas, FFmpeg/x264; có dùng Chromium qua công cụ Remotion để kiểm tra phát video.
- Không gọi API trả phí hoặc dịch vụ cloud inference.

Kiểm tra phát trình duyệt là kiểm tra kỹ thuật, không thay cho đánh giá cảm xúc âm thanh bằng tai.
