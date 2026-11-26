# Sao chép kỹ năng trong 24 giờ — bản dựng 2.5D sửa lại

## Sản phẩm thực tế

- MP4: `/workspace/outputs/skill-copy-24h-20261126/revision-v2/final/Sao_Chep_Ky_Nang_24h_Cinematic_2_5D_720p.mp4`.
- Thời lượng đo được: **469.167 giây (7 phút 49 giây)**; 16:9, **1280×720 gốc**, 24 fps, 11,260 khung hình. Đây là bản 720p, không phải bản Full HD.
- H.264/yuv420p và AAC stereo 48 kHz; 88,023,564 byte (83.95 MiB).
- SHA-256 MP4: `1a88e598f1376fb923326424b3e56f640936b57edc095b542f7a5b7655adaa1e`.
- Giữ đầy đủ 136 đoạn, 1.852 tiếng theo cách đếm dấu cách; 199 cụm phụ đề tiếng Việt được vẽ trong phim và có bản SRT riêng.

## Những phần đã làm lại

Nhân vật được vẽ lại theo góc 3/4 với tỷ lệ người trưởng thành, áo khoác sáng, quần dài và giày trắng. Có thêm chuyên gia lớn tuổi và vận động viên có vóc dáng khác biệt. Mỗi mô hình dùng bộ xương Rigby gốc 43 xương, gồm 20 xương ngón tay; chuyển động được điều khiển trong runtime, không phải slideshow hay kéo cả ảnh nhân vật.

Động tác bắt tay có chuẩn bị, chạm, nhả và ổn định; bước chân có pha tiếp đất và chuyển trọng tâm. Ngồi đàn có bước lùi, hạ người, đặt cổ tay rồi mới đánh phím. Điện thoại và dụng cụ theo bàn tay; phản ứng thay đổi theo tình huống thay vì liên tục vung hai tay. Cảnh cứu hộ cho robot mở cổng kẹt rồi hỗ trợ nhân vật bước ra, có kỹ sư bị thương hướng dẫn.

12 bối cảnh riêng cho câu chuyện dùng nền, vật thể và tiền cảnh nhiều lớp, phối cảnh, vùng sáng và bóng vẽ, camera cận/trung/toàn và dịch chuyển theo hành động. Đây là hoạt hình 2D tạo chiều sâu 2.5D bằng lớp cảnh, không phải mô hình 3D với ánh sáng vật lý hoặc chuyển động ghi từ diễn viên. Chưa thể coi thao tác đàn, cơ khí hoặc cứu hộ là mô phỏng chuyên môn chính xác.

## Lời kể và âm thanh

Lời kể do **VieNeu-TTS v3 Turbo**, bản ONNX fp32 Apache-2.0, SDK 3.8.4 chạy CPU cục bộ tạo. Tên chọn là **Minh Quân**, được adapter ánh xạ rõ ràng sang preset chính thức **Hải Đăng**. Không gọi dịch vụ suy luận từ xa. Model revision: `61b85e3d937fbbacb387714180e8182823512523`; trọng số nằm ngoài Git.

Giữ nguyên tệp lời kể đã dùng trước lần sửa hình ảnh, SHA-256 `353fb665d5f809907e612538e99bac75e3e650f4608edd2f8c89902edd2b5172`. Nhịp đọc được biên tập bằng khoảng nghỉ và thay đổi tốc độ có giữ cao độ. SDK này không cung cấp điều khiển cảm xúc bằng nhãn đang hoạt động; không bảo đảm diễn xuất như diễn viên lồng tiếng.

Nhạc và lớp foley/không khí do code tổng hợp cục bộ, cùng 11 cue chọn từ Wyzowl SFX Kit CC0-1.0. Danh sách nguồn, giấy phép và hash được giữ trong `sfx-timeline.json` và `mix-manifest.json`. Không dùng nhạc thương mại hoặc API trả phí. Phần lớn âm thanh đặt giữa hai kênh, không phải bản thu không gian surround.

## Kiểm tra thực tế

- 20 phần render có checkpoint và cùng chữ ký nguồn; ghép được đủ 11,260 khung hình. Runtime không ghi nhận lỗi trang hoặc request thất bại.
- Kiểm tra 136 shot trong trình duyệt; phát lại cùng thời điểm cho kết quả xác định. Kiểm tra 3.770 mẫu tư thế: chiều dài xương, mục tiêu IK, chân trụ, đầu gối khi ngồi và khuỷu tay khi nâng đều qua các điều kiện đã đặt.
- FFprobe đếm toàn bộ khung hình, FFmpeg giải mã hết video và audio không báo lỗi. Đã lấy 12 khung hình từ MP4 mã hoá để kiểm tra bắt tay, đàn, nấu ăn, thể thao, học tập, cứu hộ và kết phim.
- Chromium phát và tua trực tiếp MP4 tại đầu phim, cứu hộ và kết phim; không báo lỗi media. Đây là kiểm tra kỹ thuật có tắt loa, không phải nghe đánh giá toàn bộ bằng người.
- Audio Quality Report: đạt; AAC trong MP4 đo được **-14.0 LUFS**, true peak **-1.9 dBTP**; master có 0 mẫu clipping. Số đo sự kiện dùng marker tác giả, không phải hệ thống tự nhận diện va chạm trong ảnh.
- Phụ đề dựa trên thời lượng từng đoạn lời kể đã đo; thời điểm các cụm trong đoạn được chia theo tỷ lệ, chưa forced-align từng từ/âm vị.

Đã tái sử dụng lời kể và checkpoint để tránh tạo lại không cần thiết. Giữ nguyên các phim cũ và skill đã cài; bản sửa nằm trong thư mục riêng. Kiểm tra kỹ thuật không đồng nghĩa mọi khung hình đã được duyệt thẩm mỹ hoặc chuyển động đạt mức sản xuất điện ảnh chuyên nghiệp.
