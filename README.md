# Trì hoãn → Hành động · Review V3

Bản sửa theo đủ 12 điểm nhận xét. 1920×1080, 24 fps, video CBR 10 Mbps, khoảng 5:50; nhanh hơn bản trước 30 giây mà không tăng tốc giọng đọc. File PREVIEW chỉ để xem nhanh; dùng MP4 trong gói MASTER cho bản xuất chất lượng cao.

Đã sửa checkbox bằng nét vẽ, đồng nhất “cậu”, thêm hook trước giây 15, thêm SFX mở đầu, làm sinh động ba minh họa nghiên cứu, bổ sung màn kết khoảng 8 giây và CTA bình luận. Phụ đề ngắt theo cụm ý và có nền/viền tối; rim light và áo Minh sáng hơn; font UI thống nhất, ngày và split-screen rõ hơn. Nhạc/SFX tổng hợp cục bộ; model VieNeu v3 Turbo ONNX CPU, không API trả phí. 37 WAV gốc giữ nguyên; 2 lời dẫn sửa đại từ, thêm hook và CTA.

Khoảng yên của lời nói dài nhất đo RMS 10ms: 1,12 giây; khoảng chờ biên tập được rút về tối đa 0,85 giây. Âm thanh master hướng tới −14 LUFS, kiểm tra chi tiết trong QA. Phụ đề bám thời lượng chunk giọng và điểm năng lượng thấp, chưa phải forced alignment từng từ. Các kiểm tra tự động/phát trình duyệt không thay thế đánh giá nghe thủ công.

Màn kết đã chừa vùng video gợi ý và đăng ký. Khi đăng YouTube, thêm liên kết end screen thực tế trong YouTube Studio. Nguồn khoa học đầy đủ ở YOUTUBE_DESCRIPTION.md. Truy vấn đối chiếu Crossref bị proxy chặn (api.crossref.org, HTTP403); không tuyên bố đã xác minh metadata trực tuyến trong lần này.

ZIP chứa nguyên MP4 master, giải nén không giảm chất lượng. SHA256SUMS.txt dùng để kiểm tra. Nếu phải chia phần, chạy `python join_master.py` trong cùng thư mục với toàn bộ các part để ghép rồi giải nén. API GitHub Releases hiện trả HTTP403 nên cung cấp qua nhánh tải riêng, không thay đổi main hoặc phim cũ.
