# Căn cứ gaming bí mật — bản Shorts tiếng Việt

Video hoàn chỉnh: **55.77 giây**, **1080×1920**, **30 FPS**, **1673 khung hình**. File: `Can_Cu_Gaming_Bi_Mat_Shorts_1080x1920_6tieng.mp4`. Dung lượng: 11,301,901 byte, dưới giới hạn100MiB của GitHub. Không chia nhỏ file, không dùng Git LFS.

## Nhịp kể và nội dung

Giữ nguyên18 đoạn lời kể do người dùng cung cấp;26 cảnh theo trình tự shot list. Mục tiêu6,4 tiếng/giây trong phần có lời, trung bình thực tế **6.025 tiếng/giây** tính cả khoảng nghỉ. Cách đếm: 336 token tiếng Việt phân cách bằng khoảng trắng / thời lượng WAV. Khoảng im lặng dài nhất đo ở ngưỡng−35dB:0,372giây.

Giọng được tạo thực tế bằng **VieNeu-TTS v3 Turbo**, ONNXfp32, CPU, hoàn toàn offline. Model`pnnbao-ump/VieNeu-TTS-v3-Turbo`, revision`61b85e3d937fbbacb387714180e8182823512523`, giấy phépApache-2.0. Tên yêu cầu **Minh Quân** hiện được adapter cục bộ ánh xạ sang preset gốc **Hải Đăng**; không khẳng định có một preset upstream Minh Quân riêng. Tốc độ được chỉnh giữ cao độ; có khoảng nghỉ ngắn theo câu. Không dùng cloud inference hay API trả phí.

## Hình ảnh và âm thanh

Nhân vật chính43 xương,20 xương ngón tay; mẹ có artwork riêng trên cùng topology. Có chuyển động độc lập ở chân, gối, tay, cổ, đầu, mắt và ngón tay; đồ cầm theo vị trí xương bàn tay. Cảnh phòng ngủ, kho gaming và phòng khách được vẽ riêng bằng code; có mặt cắt bố trí để giải thích không gian. Ánh sáng cách điệu, camera reframing và các lớp parallax độc lập. Đây là **hoạt hình2D/2.5D theo lớp**, không phải phim render3D vật lý. Một số cảnh thiết bị/cắt lớp dùng đồ họa giải thích bên cạnh các cảnh nhân vật diễn xuất.

Có17 cueSFX được chọn từ metadata của Wyzowl SFX Kit **CC0-1.0**; nhạc và foley quạt/máy tính/cửa được tổng hợp cục bộ bằng code, không lấy nhạc thương mại. Chọn lại các cue sau khi kiểm tra để phân biệt tiếng gõ dài, thông báo thắng và thông báo lỗi. Không chèn whoosh vào mọi cú cắt.

## Kiểm tra sản phẩm thực tế

- Giải mã toàn bộ MP4 thành công; đúng kích thước, số khung hình và thời lượng; không phát hiện đoạn đen theo blackdetect.
- Mở và phát MP4 trong Chromium ở đầu, đoạn thông gió và cuối; không có lỗi phát hoặc frame rơi trong các cửa sổ thử. Đây là kiểm tra phát kỹ thuật có tắt tiếng, không phải tuyên bố đã nghe toàn bộ phim.
- Trích và xem26 ảnh trực tiếp từ MP4; sửa góc nhìn thân máy tính và nét thừa của biểu tượng Wi-Fi, chỉ render lại2 checkpoint liên quan. Bản xuất trước sửa vẫn được giữ riêng.
- 2093 tư thế kiểm tra: chiều dài xương ổn định, sai số đầu IK <0,001 đơn vị,0 wrist projection, cả2 gối cùng hướng trước, khuỷu tay bê thùng mở ra ngoài. Kiểm tra số học không tự chứng nhận mọi động tác đạt chất lượng nghệ thuật cao cấp.
- Kiểm tra vùng an toàn phụ đề ở26 điểm mẫu và khoảng cách tiếp xúc tay–đồ vật ở các động tác trọng yếu. Phụ đề dựa trên thời lượng câu thực đo với nhóm tối đa7 token; **chưa forced-align từng từ/âm vị** và chưa chạyASR đối chiếu toàn bộ lời đọc.
- Âm thanhAAC cuối: **-14.0 LUFS**, **-1.9 dBTP**,0 mẫu clipping. Kiểm tra cue theo marker khung hình; không phải hệ thống tự nhận biết tiếp xúc từ ảnh hay bảo đảm cảm nhận nghe chủ quan.
- Bộ kiểm tra Rigby13/13; bộ môi trường10/10; rig mẹ validate không lỗi. Tất cả trọng sốTTS nằm ngoàiGit. Các dự án và video cũ được giữ nguyên.

## File và bằng chứng

- MP4 cục bộ: `/workspace/outputs/gaming-secret-room-20261126/final-refined/Can_Cu_Gaming_Bi_Mat_Shorts_1080x1920_6tieng.mp4`
- Phụ đề: `captions.vi.srt`.
- SHA-256 MP4: `3f4d2234b96dd61f908f4b178988ccb48633441a8d5544b01dfcd51185332864`.
- SHA-256 lời đọc: `bb174ae6b794441e728469f3cf2ef7747eddf8323343a4317c93ecc943856958`.
- Các báo cáo đầy đủ trong `/workspace/outputs/gaming-secret-room-20261126/qa-refined/`, timelineSFX trong `/workspace/outputs/gaming-secret-room-20261126/sound-v2/sfx-timeline.json`, manifestTTS trong `/workspace/outputs/gaming-secret-room-20261126/manifests/narration.json`.

Không gọi API trả phí, không dùng ảnhAI, GPU thuê hoặc dịch vụ inference đám mây.
