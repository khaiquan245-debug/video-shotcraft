# So sánh nhịp kể — Tô ngũ cốc FAST V2

Đúng video người dùng vừa gửi đã được kiểm tra checksum và trùng mẫu phân tích trước. Áp dụng làm chuẩn Shorts của dự án, không gọi đó là quy định chính thức của YouTube.

| Chỉ số | Mẫu tham khảo | Ngũ cốc V1 | Ngũ cốc FAST V2 |
|---|---|---|---|
| Thời lượng | 38,22 giây | 40 giây | 31.2 giây |
| Tiếng tách theo khoảng trắng | 191 | 154 | 154, giữ nguyên |
| Mật độ lời trên toàn phim | ≈5,00/giây | 3,85/giây | 4.94/giây |
| Khoảng yên dài nhất trên track giọng, RMS<0,003 | Không có track riêng tương đương | 2,45 giây | 0.56 giây |

Trong phần có lời, khoảng yên liên tục lớn nhất của FAST V2 đo cùng ngưỡng là 0.25 giây. Mật độ tiếng đếm theo khoảng trắng là gần đúng, không phải âm tiết ngữ âm hay điểm chất lượng. Không so trực tiếp khoảng hở ASR của mẫu với RMS của các track giọng riêng.

## Cách sửa

Bản cũ dành quá nhiều thời gian cho khoảng yên và phản ứng kết. Lời native 37.6 giây được giữ file gốc, chỉ xử lý vào tệp mới. Thu gọn biên câu với đệm 40/45 ms, đổi khoảng nối 180 ms thành 40 ms, cho bản ghép 32.405 giây; sau đó atempo=1.058987 cho giọng 30.606 giây, giữ cao độ. Không xóa từ hoặc thêm lời mới.

Phim được render lại 936 frame ở 30 fps,1080×1920, từ cùng nhân vật/bối cảnh/rig. Nhịp các cảnh đổi theo câu đã chỉnh; giữ hành động qua biên câu mượt bằng clock cảnh riêng. Caption dùng clock audio. SFX được tổng hợp lại tại thời điểm tiếp xúc mới; nhạc chuyển sang ấm và ngắt trước cú hé lộ theo timeline mới. Ba tiếng gõ được đồng bộ với xung bàn tay/ripple ở clock thật.

Model thực tế: VieNeu-TTS v3 Turbo, ONNX CPU offline, giọng Hải Đăng; Minh Quân là alias trong adapter hiện tại. Không gọi model hoặc API mới trong lần chỉnh này. Không tái sử dụng soundtrack hoặc hình ảnh từ mẫu.

## Kiểm tra thật

- MP4 31.200 giây, 936 frame, H.264/AAC 48 kHz; giải mã toàn bộ thành công.
- -14.2 LUFS, true peak -2.0 dBTP.
- Rig: 5462mẫu, 0đích ngoài tầm, sai số chiều dài xương tối đa 1.99e-13.
- SHA-256:`a7e811b11d0f0228d66a5e7a4e464c2fd8dac78bf84466cc1cbb24a7d468eb1e`.
- Kiểm tra ảnh từ chính MP4 ở các nhịp thìa/mèo/hộp/dây/gõ; phát thử Chromium 1× để kiểm tra kỹ thuật. Phiên phát tắt tiếng; không tự nhận đã duyệt cảm xúc hoặc độ dễ nghe bằng tai người.

Phụ đề có 43cụm nghĩa; biên câu theo đoạn TTS thực tế, biên cụm trong câu ước lượng, chưa forced alignment từng từ. Không chứng nhận tương đương thẩm mỹ/giọng với mẫu. Bản40 giây và WAV native giữ nguyên. Model weights nằm ngoài Git. Chuẩn dùng lại ở `/workspace/outputs/production_rules/SHORTS_NHIP_KE_NHANH.md`.
