# Nếu Việt Nam mất điện 7 ngày — bản bối cảnh Việt Nam

Video giả định theo kịch bản người dùng. File xem/tải: **Viet_Nam_Mat_Dien_7_Ngay_1080x1920.mp4**.

- 1080 × 1920, 30 FPS, 1.264 khung hình, 42.133 giây, H.264/AAC 48 kHz.
- 23 shot; phụ đề tiếng Việt được đốt vào hình và kèm SRT với 70 cụm ý.
- 278 đơn vị tiếng Việt cách bằng khoảng trắng / 42,133 giây = 6,598 tiếng/giây; không phải phép đo âm vị.
- Dung lượng MP4: 9,074,581 byte. SHA-256: `8871cc7fb8d745c66762255c5491bac29ca10f2f7f5c2443fbbe15a4b91ddaac`.

## Thay đổi hình ảnh

Nhà ống, mái bằng, bồn nước, ban công, cửa cuốn, dây điện, cờ Việt Nam, xe máy có người đội mũ bảo hiểm, biển hiệu tiếng Việt và tạp hóa. Bếp, trạm xăng, bệnh viện, nhà máy, kho hàng có đạo cụ riêng gắn với lời kể. Thêm thảm, gạch lát, hàng thiết yếu và vạch sàn; bỏ phần đất trống lặp lại trong nhà. Khung hình tập trung vào hành động; cảnh cuối cho thấy cáp điện liên kết nhà cửa và các dịch vụ. Không có góc quay từ trên cao.

Nhân vật chính sử dụng nhiều bộ phận và khớp Rigby2D bản địa; đồ vật theo vị trí cổ tay. Xe và bánh xe có chuyển động riêng, đèn/cánh quạt/máy móc/màn hình đổi trạng thái theo từng cảnh. Các người đi xe máy phía sau là hình vẽ ngồi cố định đi theo xe, không phải nhân vật được rig đầy đủ. Đây là hoạt hình vector nhiều lớp, không phải mô phỏng 3D vật lý hoặc bản sao 100% video tham khảo.

## Giọng và âm thanh

VieNeu-TTS v3 Turbo, mô hình Apache-2.0, ONNX chạy CPU cục bộ, không gọi inference đám mây. Tên chọn **Minh Quân** là alias của preset thực tế **Hải Đăng** (nam Bắc, tự nhiên); xem native-tts-engine.json. WAV gốc 66,22 giây được giữ nguyên trong thư mục sản xuất; WAV làm việc tách riêng, xử lý khoảng lặng và tempo giữ cao độ 1,468532 để đạt nhịp đã yêu cầu. Không thay thế lời đọc cũ đã duyệt.

Nhạc nền và foley được tổng hợp cục bộ riêng cho video. 8 cue Wyzowl được chọn từ metadata, 4 asset CC0, bám các marker hành động; có chứng cứ nguồn/license/hash. Không lạm dụng whoosh hay cinematic hit. Phối âm có ducking lời đọc. Master WAV kèm theo; không bao gồm trọng số mô hình.

## Kiểm tra đã chạy

- Kiểm tra tất cả khung hình khi render: không có lỗi WebGL, caption vượt biên hoặc IK reach projection.
- 819 mẫu pose: không lỗi chiều dài xương, trượt chân khi đứng hoặc khuỷu gập vào trong. Bộ test Rigby 13/13 và môi trường 10/10 đạt.
- 70 cue phụ đề: chiều rộng lớn nhất 739,52 / 900 đơn vị khung hình; lề ngang tối thiểu khoảng 96 pixel khi xuất 1080.
- Proof chuyển động 5,5 giây ở độ phân giải gốc được kiểm tra trước khi hoàn tất. Đã sửa lỗi đường vẽ nối sai từ mũ bảo hiểm và bố cục trống trong lần kiểm tra.
- Đã giải mã toàn bộ MP4 cuối, kiểm tra số khung hình và các đoạn đen: không lỗi, không phát hiện khung đen. Đã xem ảnh trích từ 23 shot và các mẫu tiếp xúc điện thoại/POS, cốc/cổ tay, cùng nhãn ngày ở cảnh đêm. Điều chỉnh tương phản nhãn ngày bằng bước finishing FFmpeg, không đổi timeline hay giọng.
- Âm thanh MP4 cuối: -14.0 LUFS; -1.8 dBTP; kiểm tra âm thanh PASS. Không có lỗi cảnh báo trong báo cáo.
- Build Vite riêng cho dự án thành công; chỉ có cảnh báo bundle trên 500 kB, không ảnh hưởng MP4.

Giới hạn: phụ đề bám mốc câu đo từ WAV và chia cụm ý theo tỷ lệ, không phải forced alignment từng từ/âm vị. Cue âm thanh được đồng bộ với marker do tác giả đặt, không phải tự phát hiện tiếp xúc bằng thị giác. Các phép đo kỹ thuật không thay cho việc nghe/duyệt cảm nhận toàn bộ phim của con người. Mạng điện và chuyển động năng lượng mang tính minh họa, không phải sơ đồ kỹ thuật hoặc mô phỏng tốc độ điện.

## Bảo toàn và nguồn

Dự án mới: `/workspace/video-shotcraft/integrations/vietnam-blackout-7days/` và `integrations/pixijs-environment/projects/vietnam-blackout/`. Thư mục sản xuất: `/workspace/outputs/vietnam-blackout-7days-20261127/`. Bản hình và bản mux trước khi chỉnh nhãn ngày được giữ để đối chiếu. Video tham khảo chỉ dùng nghiên cứu nhịp và phong cách; không lấy lại hình, nhạc hoặc giọng của video đó. Không sửa dự án cũ hoặc skill, không dùng API trả phí. Trọng số TTS nằm ngoài Git tại `/workspace/tts-runtime/models/`. Bản tải GitHub được tạo trên nhánh tải riêng; không merge/push main.
