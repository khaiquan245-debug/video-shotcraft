# Báo cáo thực tế — Màn hình cảm ứng

## Thành phẩm

`Man_Hinh_Cam_Ung_44_2s_1080x1920.mp4` đã render: **44.2 giây, 1326 khung hình, 1080×1920, 30fps, H.264 yuv420p, AAC stereo48kHz**, 3,992,148byte.

SHA-256: `bc636f50a61390611e183fc0ac41fbf26c3881dc12af2f8ee9ba490a6758a58a`.

17 đoạn lời kể theo thứ tự nguyên bản; có ẩn/hiện lớp kính và lưới điện cực, đầu ngón tay tiếp xúc, điện trường minh họa, bộ điều khiển quét tín hiệu, tọa độ bám điểm chạm, kéo ảnh/cuộn/phóng to hai điểm, ví dụ găng tay không nhận. Nhân vật và tay có chuyển động; không dùng slideshow ảnh.

## Giọng và nhịp

Giữ nguyên221tiếng theo cách đếm khoảng trắng. TTS gốc **50.64giây** được bảo toàn. Rút khoảng im lặng đầu/cuối câu, nối45ms rồi dùng atempo **1.036872** giữ cao độ. WAV sau chỉnh **43.805604giây**; video44,2giây≈5,00tiếng/giây. Nhịp tham khảo riêng từ video191tiếng/38,220045giây; không xem đây là quy tắc YouTube chung.

Model thực sự tạo WAV: **VieNeu-TTS v3 Turbo**, backend **onnx**, CPU ngoại tuyến. Tên yêu cầu **Minh Quân** là alias preset **Hải Đăng** (nam Bắc tự nhiên), không thay model. Có WAV gốc/chỉnh nhịp và metadata đã loại đường dẫn nội bộ không cần thiết.

Phụ đề một dòng chia cụm nghĩa, theo các khoảng câu đã đo từ audio. Nối phụ đề khớp kịch bản. Không có forced alignment từng từ; không tuyên bố chính xác từng âm tiết.

## Kiểm tra thực tế

- FFprobe xác nhận đầy đủ kích thước/codec/tốc độ/1326khung hình.
- FFmpeg giải mã toàn bộ tệp: qua.
- Độ lớn đo từ MP4: **-14.1LUFS**, true peak **-1.7dBFS**.
- Khoảng yên voice lớn nhất theo RMS0,003/cửa sổ10ms: **0.36giây**. Chỉ là chỉ báo năng lượng, không phân tích âm vị.
- Giải khớp hai tay/hai chân ở các khung có nhân vật: 280phép giải, 0mục tiêu ngoài tầm, sai số chiều dài xương tối đa 3.55e-14.
- Đã sửa vị trí chân đứng trên sàn và tránh chữ chồng ở giả thuyết nút bấm trước bản xuất cuối. Bỏ ký tự mũi tên không có trong font; giữ dấu tiếng Việt và Delta có trong font. Chỉnh vùng di chuyển tay ở mặt cắt để không che tiêu đề.
- Cắt vùng ảnh từ **MP4 thực** để đo: ảnh vùng màn hình sau găng tay chạm chênh lệch RGB trung bình **0.0000/255** (ngưỡng2,5); mở ảnh bằng tay trần **22.1788**, kéo ảnh **38.5327**, phóng to **14.3078**. Các kiểm tra vùng ảnh xác nhận phản hồi/không phản hồi đã chọn, không tự chứng minh toàn bộ chất lượng mỹ thuật.
- Ví dụ nội suy nhiều điện cực có sai lệch tâm trọng số tối đa **0.000131** theo tọa độ chuẩn hóa. Khoảng cách hai điểm minh họa tăng70→165.94px cùng ảnh tăng tỷ lệ1→1,65.
- Có contact sheet lấy từ MP4 mã hóa, kiểm tra phụ đề/rig và báo cáo Chromium phát1× đến cuối. Kiểm tra trình duyệt tự động tắt tiếng; không có thẩm âm bởi người và không tuyên bố người dùng đã duyệt.

## Phạm vi khoa học và giới hạn

Phim mô tả **cảm ứng điện dung phổ biến** bằng sơ đồ giản lược; không áp dụng khẳng định không đo lực cho mọi điện thoại/công nghệ màn hình. Một số thiết bị có phần cứng đo lực riêng; cảm ứng điện trở ngoài phạm vi phim.

Lưới8×10 chỉ để nhìn rõ cơ chế, không phải số điện cực/độ phân giải thật. Mô hình nội suy là ví dụ, không phải firmware hãng. Điện dung ở các điện cực có thể tăng/giảm tùy kiểu đo; thanh minh họa chỉ thể hiện độ lớn thay đổi, không phải giá trị hay chiều thay đổi phổ quát. Ngưỡng/đường sức minh họa không phải đo đạc vật lý. Găng tay thường có thể không nhận; loại dẫn điện có thể hoạt động. Âm tín hiệu là sonification, không phải tiếng thật của điện trường/cảm biến.

## Bảo toàn và chi phí

Tất cả tệp mới nằm trong dự án touchscreen riêng; không sửa Video Shotcraft, skill hoặc video ATM/dự án cũ. Model weights ở runtime ngoài Git. ZIP không có weights/secrets/video tham khảo. Mọi asset/nhạc/SFX mới tạo tại máy, không gọi API hay thuê bao/GPU trả phí.
