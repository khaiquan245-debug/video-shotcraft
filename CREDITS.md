**Nguồn và quyền sử dụng**

- Kịch bản, tạo hình, bối cảnh và mã diễn hoạt: tạo mới cho video mẫu này.
- Video người dùng cung cấp chỉ dùng phân tích nhịp và cách dàn cảnh, không tái sử dụng hình hoặc soundtrack trong phim mới.
- Nhạc pluck, mưa, tiếng gỗ/đất/nước/ếch: tổng hợp bằng oscillator/noise local trong `production/audio.py`; không dùng bản nhạc bên thứ ba.
- Giọng: VieNeu-TTS v3 Turbo, model Apache-2.0, ONNX CPU offline; preset Minh Quân → Hải Đăng. Trọng số ở ngoài Git.
- Font Nunito theo SIL Open Font License; giấy phép được giữ trong assets/OFL-Nunito.txt của dự án.
- Công cụ: Node/@napi-rs/canvas, Python/NumPy, FFmpeg/x264; Chromium qua Remotion dùng kiểm tra phát.
- Không gọi API trả phí, không cloud inference.
