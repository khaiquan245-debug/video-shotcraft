# Biệt thự cho mèo — báo cáo bản xuất thực tế

- MP4: `Biet_Thu_Cho_Meo_Cai_Ket_1080x1920.mp4`.
- Thời lượng 38.46667s; 1080×1920; 30fps; 1154 khung hình; H.264/AAC, 48kHz stereo.
- 9,329,174 byte; SHA-256 `a24f7b3b726953f6e21ab5d2528d0b9bf874c649684954ac52fbcd514bf48b33`.
- Giữ nguyên 12 đoạn lời kể; 25 shot theo tiến trình xây nhà, mở rộng, mèo chọn thùng carton và người sử dụng nhà mèo.
- Nhịp thực đo 6.577 token tiếng Việt/giây trên toàn timeline (xấp xỉ6,6); nhịp từng câu có ngắt nghỉ ngắn.
- VieNeu-TTS v3 Turbo, ONNX fp32 CPU, SDK3.8.4, Apache-2.0; model `pnnbao-ump/VieNeu-TTS-v3-Turbo`, revision61b85e3d937fbbacb387714180e8182823512523. Tên Minh Quân trong cấu hình hiện tại là alias của preset gốc Hải Đăng. Không dùng giọng từ video tham khảo hoặc dịch vụ trả phí.
- Native Rigby: người23 xương, mèo22 xương. Đầu, tai, mắt, đuôi và bốn chân mèo chuyển động độc lập; IK tay/chân người, fixed bone lengths. Bối cảnh và props lập trình riêng, xây dựng tích lũy qua các cảnh; góc nhìn rộng hơn30% so với framing cơ sở. Đây là hoạt hình2D cắt lớp, không phải phim dựng3D vật lý.
- Kiểm tra: native cat validate không lỗi/cảnh báo;1963 mẫu tư thế người và1446 mẫu mèo không IK projection, sai số số học chiều dài/tip<1e-10;25 shot kiểm tra khung hình mã hóa và safe area phụ đề;10 contact markers mẫu đều sai số<4 world units. Số học không bảo đảm mọi khung hình đều tự nhiên.
- MP4 giải mã đầy đủ, không phát hiện đoạn đen; phát thử file mã hóa ở mở đầu, mèo vào thùng và kết thúc không lỗi/khung rơi trong bài kiểm tra trình duyệt.
- Âm thanh:18 marker chọn từ Wyzowl CC0, cùng nhạc vui và foley tổng hợp offline nguyên bản; âm lượng mux thực đo -14.0 LUFS, -2.0dBTP;0 mẫu clipping. Có cảnh báo lặp wood-touch: chủ ý cùng vật liệu và chuỗi xây dựng, không dùng whoosh liên tục.
- Đã sửa hai tên category âm thanh không khớp catalogue trước khi phối; các lần plan lỗi được giữ trong thư mục sound/sound-v2, bản thành công ở sound-final. Không có tải model/network/API trong quá trình tạo phim.
- Phụ đề dựa trên độ dài câu đo thực tế và nhóm ngắn chia theo tỷ lệ, không phải forced alignment từng từ/âm vị. Playback kỹ thuật được tắt tiếng; không tuyên bố đã kiểm định nghe chủ quan toàn phim.
- Weights nằm ngoài Git. Các project, WAV được duyệt và phim cũ được giữ nguyên. Không dùng API, GPU hay tài sản trả phí.

Đường dẫn bản đầy đủ trong Codex: `/workspace/outputs/cat-mansion-20261126/final/Biet_Thu_Cho_Meo_Cai_Ket_1080x1920.mp4`.

Mã nguồn dự án mới: `/workspace/video-shotcraft/integrations/cat-mansion/` và `/workspace/video-shotcraft/integrations/pixijs-environment/projects/cat-mansion/`.
