# Báo cáo thực tế — Bên trong máy ATM

## Sản phẩm

- Tệp đã xuất: `Ben_Trong_May_ATM_38_2s_1080x1920.mp4`.
- 38.2 giây, 1146 khung hình, 1080×1920, 30fps, H.264 yuv420p, AAC stereo 48kHz.
- Dung lượng: 3,755,772 byte.
- SHA-256: `85cd55814b31295818ebcd5b39fbab15bc9c28f7b0b3463e6f2f423662351f0b`.
- MP4 có lời kể, nhạc tự sáng tác, 45 cue SFX và phụ đề tiếng Việt. Có hoạt hình khớp nhân vật, di chuyển thẻ, tiền theo đường dẫn, bánh lăn quay, cảm biến/gạt và bộ đếm; không phải slideshow ảnh.

## Giọng kể và nhịp

Toàn bộ 191 tiếng theo cách đếm khoảng trắng được giữ nguyên. File TTS gốc 44.32 giây được bảo toàn; chỉ cắt im lặng đầu/cuối câu, nối khoảng nghỉ 45ms rồi dùng `atempo=1.066005` giữ cao độ. Bản voice sau xử lý dài 37.806 giây; phim 38,2 giây ≈5,00 tiếng/giây, gần video tham khảo 38,220045 giây với191tiếng. Đây là chuẩn nhịp tham khảo riêng của dự án.

Model thực tế: **VieNeu-TTS v3 Turbo**; backend **onnx**, CPU, ngoại tuyến. Voice adapter yêu cầu **Minh Quân**, preset thực tế **Hải Đăng** (nam Bắc tự nhiên). Không dùng model khác thay thế. WAV gốc và metadata/hashes kèm gói.

Phụ đề chia cụm nghĩa một dòng, canh từ thời lượng từng câu đã đo. Chưa thực hiện forced alignment từng từ; không tuyên bố độ chính xác từng âm tiết.

## Hình và tính nhất quán

Nhân vật áo cam, tóc đen, quần xanh và giày vàng giữ thiết kế. Hai xương trên mỗi tay/chân; kiểm tra tất cả khung hình có nhân vật: 1440 phép giải, 0 mục tiêu ngoài tầm; sai số chiều dài xương tối đa 4.97e-14. Đã kiểm tra contact sheet bản mã hóa và các thời điểm đưa thẻ, nhập mã, tiền qua cảm biến, tách vào ngăn riêng, trả thẻ và nhận tiền.

Thẻ chỉ có chip/dấu chấm giả lập, mã xác thực được che. Số tiền minh họa: **5×200.000đ =1.000.000đ**. Có một ví dụ tờ không đạt; nó không được tính vào 5 tờ trả ra, sau đó một tờ hợp lệ thay thế. `qa/money-accounting.json` ghi lịch từng tờ. Mọi tờ bắt đầu di chuyển sau chấp thuận.

**Sơ đồ cơ khí giản lược; không đại diện một mẫu ATM/ngân hàng cụ thể.** Xử lý kẹt, điều kiện giao dịch, thứ tự trả thẻ/tiền và khả năng cảm biến có thể khác nhau. Cảnh loại tờ không phù hợp không khẳng định mọi lỗi kẹt đều có thể tự chuyển ngăn, không đưa ra tuyên bố phát hiện tiền giả.

## Kiểm tra kỹ thuật

- FFprobe: đúng kích thước, tốc độ hình, codec và 1146 khung hình.
- FFmpeg giải mã toàn bộ tệp: qua, không báo lỗi.
- Loudness đo từ MP4 AAC: **-14.2 LUFS**, true peak **-2.0 dBFS**.
- Khoảng yên lời kể dài nhất theo ngưỡng RMS0,003 trên cửa sổ10ms: **0.35 giây**. Đây là chỉ báo năng lượng, không phân tích âm vị.
- Phụ đề nối lại khớp chính xác kịch bản; đo bề rộng raster trước render, không tràn vùng650px thiết kế.
- Có ảnh lấy từ MP4 cuối cùng, log rig, loudness và báo cáo phát kỹ thuật Chromium1× đi kèm gói.

## Giới hạn kiểm tra

Đã xem các khung hình thực tế và kiểm tra kỹ thuật phát trọn tệp. Trình duyệt được chạy ở chế độ tắt tiếng cho kiểm tra tự động; không có nghe thẩm âm bởi người và không tuyên bố người dùng đã duyệt thẩm mỹ. Hoạt hình2D sơ đồ gốc, không phải ảnh quay cơ khí thực hay mô phỏng một ATM thương mại cụ thể.

## Bảo toàn

Không thay đổi Video Shotcraft, skill đã cài hoặc dự án cũ. Tất cả tệp mới trong thư mục ATM riêng. Trọng số ở runtime ngoài Git; ZIP không chứa mô hình, secrets hay video tham khảo. Không dùng API, thuê bao hay GPU trả phí.
