# Căn cứ xe buýt — FAST V2

MP4 **29.367giây**,1080×1920,30fps,881frame. Bản trước32,9giây; tốc độ toàn phim tăng **12.03%**. Giữ nguyên171tiếng của script, nội dung, nhân vật và bối cảnh.

18 đoạn được chỉnh tốc độ khác nhau theo câu/hành động, khoảng4–16%; thêm tổng5frame nghỉ ngắn ở các nhịp chuyển nguy hiểm/hé lộ. Giọng nguồn VieNeu-TTS v3 Turbo, ONNX CPU offline, Hải Đăng (alias Minh Quân) được dùng lại, không tạo speaker mới. FFmpeg atempo giữ cao độ, gain nhấn từ khóa dạng mượt tối đa0,8dB. Đây là biên tập nhịp/âm lượng trên giọng đã có, không phải tạo mới diễn xuất cảm xúc bằng TTS.

SFX được đặt lại theo timeline mới với độ dài âm tự nhiên; nhạc Investigations giữ nguyên94BPM, rút excerpt và duck dưới giọng mới. Phụ đề cháy trong ảnh theo các đoạn hình đã retime; SRT được remap tương ứng, sai số lấy mẫu frame khoảng1/30giây. Không forced-align từng từ.

QA: giải mã toàn file thành công, -14.2LUFS, -2.1dBTP; kiểm tra kích thước/fps/881frame, chữ script/caption nguyên vẹn và source MP4 cũ không đổi. Khớp nhân vật kế thừa các frame cũ đã kiểm tra, không phát sinh geometry mới hoặc dùng nội suy AI. Playback1× tắt tiếng là kiểm tra kỹ thuật, không chứng nhận đã duyệt nghe bằng tai người.

Không gọi API trả phí, không tạo lại asset/giọng gốc hoặc sửa installed skill. Ghi nguồn nhạc khi đăng: MUSIC_CREDIT.txt; các nguồn khác xem CREDITS.md.

SHA-256 MP4: a39242bfa2f99eea14536a0bef5a5ab71f1a01d4f567edb2ef4b847d6879b772.
