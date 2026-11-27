# Căn cứ dưới tuyết chống rét — bản xuất thực tế

- File: `Can_Cu_Duoi_Tuyet_Chong_Ret_1080x1920.mp4`.
- 45.4giây,1080×1920,30FPS,1362frames,H.264/AAC48kHz stereo; 9,984,060byte.
- SHA-256: `7ab7209c9337e869b374a5013cc7b3b74cb4c697b59d17c03fb0d2d9c97a4ff1`.
- Giữ nguyên14 đoạn kịch bản tiếng Việt;299 token tiếng Việt, nhịp thực đo6.586tiếng/giây.31shot có hành động, bối cảnh và nâng cấp tích lũy; không có khoảng hở/chồng thời gian.
- Dùng bố cục nhìn ngang, mặt cắt, nhịp nâng cấp và giải pháp→vấn đề của video mẫu. File mẫu mới có cùng SHA-2562b47c5289cbed7b4416db2c033b44561b72e4f0230fd7601812a9a944ad36ca4 với bản đã phân tích, nên dùng lại phân tích. Không nhúng cảnh, âm thanh, watermark hoặc artwork trích từ video mẫu vào bản mới. Không khẳng định giống100%.
- Artwork lập trình mới: làng tuyết, máy đào có boom/stick/bucket độc lập, tầng đất và căn hầm, khung thép, bê tông, màng chống thấm/cách nhiệt, hai cửa, đồ nội thất, thông gió thu hồi nhiệt, nguồn điện và nước tan. Đây là hoạt hình2D mặt cắt minh họa, không phải mô phỏng3D vật lý, mô phỏng nhiệt/nước hoặc bản vẽ thi công.
- Nhân vật cùng đầu/mặt/tóc của bộ đã duyệt, native Rigby23bone, trang phục dài tay/pants mùa đông ở file rig mới; rig cũ giữ nguyên. Có tay/chân, đầu, thân, phản ứng và tương tác đạo cụ; không phải slideshow.
- Đã sửa điểm chạm khung/công tắc/núm sưởi/ắc quy, grip theo tay nắm cửa đang mở và cú đổi hướng khuỷu khi uống. Bản sửa dùng cổ tay đi theo cung với pole khuỷu ổn định, chân giữ tiếp xúc.2172mẫu pose không IK projection, không trượt điểm đặt chân; sai số chiều dài xương/tip<1e-10. Chỉ số không bảo đảm mọi chuyển động tự nhiên tuyệt đối.
- Lời kể tạo offline bởi VieNeu-TTS v3 Turbo ONNXfp32CPU,SDK3.8.4,Apache-2.0,revision61b85e3d937fbbacb387714180e8182823512523. Cấu hình Minh Quân hiện tại ánh xạ preset gốc Hải Đăng; không tuyên bố đó là preset gốc tên Minh Quân. Weights nằm ngoàiGit. Không tạo lại narration sau khi đã khóa timeline.
- Phụ đề đủ toàn bộ chữ, nhóm ngắn theo thời lượng câu đo thực tế; không phải forced alignment từng âm vị/từ. Mẫu31shot nằm trong safe area đã kiểm tra.
- Âm thanh:16marker chọn từ Wyzowl CC0,10asset khác nhau; nhạc và foley nguyên bản tổng hợp offline. Master và MP4đã QC; âm lượng mux-14.0LUFS,true peak-2.1dBTP,0mẫu clipping,không cảnh báoQC.
- Kiểm tra: Rigby13/13,environment10/10,native rig validate không lỗi/cảnh báo; decode toànMP4 thành công,không đoạn đen;31ảnh lấy từ MP4và chuỗi9ảnh chuyển động uống cà phê đã xem lại.8contact sample sai số<1world unit.
- Playback thử mở đầu,cửa kép,kết thúc không media error; trình duyệt headless ghi nhận tối đa1dropped frame trong bài phát/seek dướiCPU,không đồng nghĩa file mã hóa mất khung. File có đủ1362frames. Bài phát kỹ thuật được mute; không tuyên bố đã nghe và chấm chủ quan toàn bộ mix.
- Một lỗi cú pháp trong prototype và elbow snap ở bản thử được phát hiện/sửa trước bản cuối. Render theo checkpoint; giữ nguyên file cũ và project cũ. Không dùng API,cloud inference,GPUtrả phí hoặc đăng ký trả phí.

File trong Codex: `/workspace/outputs/snow-bunker-20261127/final/Can_Cu_Duoi_Tuyet_Chong_Ret_1080x1920.mp4`.
Mã nguồn mới: `/workspace/video-shotcraft/integrations/snow-bunker/` và `/workspace/video-shotcraft/integrations/pixijs-environment/projects/snow-bunker/`.
