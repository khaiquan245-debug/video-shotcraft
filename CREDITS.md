# Nguồn và giấy phép

- Kịch bản: toàn bộ lời kể tiếng Việt người dùng cung cấp; không thêm/đổi lời.
- Nhân vật gốc, tay cận cảnh, điện thoại, môi trường và sơ đồ: vẽ bằng mã của dự án. Nhân vật áo cam tiếp nối thiết kế của video ATM trước; toàn bộ nội dung cảm ứng là mới.
- Không lấy hình/cảnh/âm thanh từ video tham khảo; chỉ dùng chuẩn nhịp kể đã thống nhất.
- Nhạc nền128BPM, âm môi trường và 37 cue SFX: tự tổng hợp tại máy bằng oscillator và noise trong production/audio.py. Không có bản ghi bên thứ ba. Các âm tín hiệu điện cực là thiết kế âm thanh minh họa.
- Nunito: SIL Open Font License1.1, font và giấy phép kèm assets/.
- VieNeu-TTS v3 Turbo: https://huggingface.co/pnnbao-ump/VieNeu-TTS-v3-Turbo — model Apache-2.0, ONNX CPU offline. Preset thực tế Hải Đăng, alias adapter Minh Quân. Không clone giọng cá nhân mới.
- Công cụ: FFmpeg, @napi-rs/canvas, NumPy, Pillow, Chromium/Remotion để kiểm tra kỹ thuật.
- Không dùng API, GPU hoặc thuê bao trả phí. Không phân phối model weights/secrets/video tham khảo.
