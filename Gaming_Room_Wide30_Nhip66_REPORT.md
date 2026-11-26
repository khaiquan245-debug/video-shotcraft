# Góc nhìn+30% · nhịp đọc6,6tiếng/giây

Video hoàn chỉnh: **50.93giây ·1080×1920 ·30FPS**, 1528khung hình.

- Vùng bối cảnh nhìn thấy rộng/cao hơn30% so với bản cutaway gốc; camera zoom chia1,3. Tâm và đường đi camera giữ nguyên; không kéo dãn nhân vật.
- Lời đọc trung bình thực đo **6.5969 tiếng/giây**, làm tròn6,6: 336 token tiếng Việt phân cách bằng khoảng trắng / thời lượngWAV. Giữ nguyên toàn bộ nội dung và giọng đã chọn.
- Chỉnh tốc độ giữ cao độ từ cácWAV cục bộ đã có, không tạoTTS mới. Hình/nhân vật/camera/đạo cụ được lấy mẫu theo cùng đồng hồ mới ở30FPS; không tăng tốc mộtMP4 cũ bằng cách bỏ frame. Phụ đề và18cueSFX được căn lại theo nhịp này.

Đã giải mã toàn bộMP4; đúng kích thước, thời lượng và sốframe. Trích26 ảnh mã hóa và đối chiếu26 điểm cùng nguồn thời gian: tư thế/tỷ lệ nhân vật, trạng thái đồ và nội dung phụ đề giữ nguyên; camera rộng hơn đúng30%. Các điểm tiếp xúc và vùng an toàn chữ được kiểm tra. Chromium mở phát file thật ở đầu, giữa và cuối, không lỗi trong các cửa sổ thử; đây là kiểm tra phát kỹ thuật có tắt tiếng.

Âm thanhAAC cuối: **-14.0LUFS**, **-2.0dBTP**,0mẫu clipping. Phụ đề dựa trên thời lượng câu đã đo, chưa forced-align từng từ/âm vị. Thư việnSFX WyzowlCC0; nhạc/foley được tạo cục bộ từ bản trước. Nguồn giọng là VieNeu-TTS v3 Turbo ONNXCPU/Apache-2.0; adapter Minh Quân ánh xạ preset gốc Hải Đăng. Trọng số ngoàiGit; không API trả phí hay cloud inference.

File: `/workspace/outputs/gaming-secret-room-wide30-66-20261126/final/Can_Cu_Gaming_Bi_Mat_Goc_Rong_30pct_Nhip_6_6_1080x1920.mp4`.
SHA-256: `92dde5040a7d8659628d880781da49403a9a969320a81459db2145ec9c4febe3`.
Dung lượng: 12,724,762byte, dưới giới hạnGitHub100MiB. Các bản trước giữ nguyên; hai lượt góc10% và góc30%/tốc độ cũ được dừng khi người dùng cập nhật yêu cầu.
Bằng chứng trong`qa/final-qa.json`, `qa/final30-66-playback.json`, `qa/retiming-and-framing.json`, `qa/final-audio/` và`manifests/film.json`.

Trình phát thử ghi nhận1frame rơi khi phát/seek trong trình duyệt; kiểm tra giải mã và ffprobe xác nhận fileMP4 có đủ1528frame.
