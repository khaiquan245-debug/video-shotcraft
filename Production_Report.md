# Kết quả thực tế — Cục tẩy xóa mọi thứ

Tệp MP4 thật **50.400 giây**, **1080×1920**, **30 fps**, **1512 frame**, H.264 yuv420p + AAC stereo 48 kHz, **6,591,819 byte**. Kịch bản đầu vào và phụ đề giữ nguyên 252 tiếng theo khoảng trắng, không thêm lời hoặc đổi thứ tự. Đây là hoạt hình vector 2D có khớp tay/chân, chuyển động đồ vật và camera.

## Nhịp theo tham chiếu

Tệp người dùng gửi lại trùng SHA-256 của bản tham chiếu 38,220 giây đã phân tích. Lời dựng lại từ mẫu có khoảng 191 tiếng, gần 5,00 tiếng/giây. Phim mới có 252 tiếng / 50,4 giây = 5,00 tiếng/giây. Nhịp thông tin, nhịp chuyển động và nhịp cắt máy được xét riêng; không ép một cut theo mọi cụm phụ đề.

Native WAV 60.920 giây được bảo toàn. Sau cắt yên ở biên câu với đệm 40/45 ms, nối 45 ms (trước câu cuối 150 ms), bản ghép 53.930 giây được xử lý atempo=1.078600 giữ cao độ, ra giọng 50.005 giây. Khoảng yên lớn nhất giữa phần có lời theo RMS<0,003 là **0.31 giây**; lớn nhất gồm cả đuôi phim **0.37 giây**. Mốc ASR của mẫu không tương đương phép đo RMS trên stem riêng, nên không tuyên bố từng khoảng dừng giống hệt mẫu.

Camera theo cục tẩy xuống dốc; đổi cỡ cảnh khi đồ vật biến mất và cậu phản ứng; theo trục dọc khi rơi, kéo rộng cho thấy đường thoát, vào cận giấu chân trước cú lộ giày cuối. Trước cú nhảy, khung hình giữ cả cậu bé, cục tẩy và miệng cống. Không dùng dissolve dài hoặc intro logo.

## Diễn hoạt và liên tục

Cùng nhân vật áo cam, mặt/tóc/đồng phục giữ ổn định. Tay/chân dùng IK hai đoạn cố định, có cúi nhặt, chà, bước/chạy, thu người lấy đà, nhảy chụp, rơi, cầm kiểm tra, xóa vách, leo từng bậc và cất cục tẩy. Một cục tẩy chuẩn bám cổ tay khi cầm, chỉ tách thành free sprite trong pha rơi/lăn. Tại mốc chụp 35.599 giây, tâm sprite tự do và cục tẩy trong tay trùng nhau, sai số **0** đơn vị thế giới.

Bàn/ghế/rác/hộp/tủ đã xóa không trở lại. Thùng chỉ bị xóa một phần trước khi tuột tay. Gạch/bậc/đất mất theo quỹ đạo cục tẩy; hố mở phía sau nó. Điểm chụp x=2419 trước cống x=2550. Bậc thoát nối từ đáy hố lên bờ trái, được mở từ điểm chà vách. Cục tẩy được cất trước cảnh giày mất; cận thân che chân trước cú lộ. Chuyển động và không gian là diễn hoạt hoạt hình, không mô phỏng vật lý hoàn chỉnh.

## Âm thanh và phụ đề

Model thực tế **VieNeu-TTS v3 Turbo**, backend **ONNX CPU offline**, preset **Hải Đăng**, alias được yêu cầu **Minh Quân**. Native SHA không đổi. Nhạc nguyên tác 130 BPM cùng **79 cue SFX** (có nhiều tiếp xúc lăn nhẹ) tự tổng hợp local; nhạc hạ dưới giọng. SFX theo nhặt/chà/xóa/tuột/lăn/sụt/chụp/rơi/leo/cất và nhấn cú giày cuối.

**80 cụm phụ đề** giữ nguyên chữ, một dòng có viền; thời điểm trong câu phân bổ theo cụm nghĩa và thời lượng câu đã đo, chưa forced-align từng từ. Đã nhận dạng kiểm tra bổ sung bằng faster-whisper-small local CPU; độ tương đồng token 89.7%. Có sai khác ASR, lưu nguyên văn trong qa/asr-comparison.json; chưa dùng tai người để phân biệt lỗi nhận dạng với lỗi phát âm.

## QA thực tế và phạm vi

- FFprobe xác nhận codec, 1080×1920, 30 fps, 1512 packet hình; giải mã toàn MP4 không lỗi.
- Âm lượng **-14.2 LUFS**, true peak **-1.7 dBTP**.
- Rig trên toàn 1512 frame: **6048 phép giải**, **0 đích ngoài tầm**, sai số chiều dài xương tối đa **5.68e-14**.
- Đã xem ảnh lấy từ draft và MP4 full ở các nhịp chính; sửa khung trước cú chụp và nét chân ở cảnh giày mất. File QA ghi phạm vi kiểm tra.
- Phát Chromium 1× tắt tiếng đến cuối, kiểm tra SHA khớp tệp final. Đây là kiểm tra giải mã/phát, không thay cho người dùng nghe đánh giá nhạc, SFX và phát âm.
- MP4 SHA-256: `86d10541d8bfeb38729eec6f9556ac5966aa7329dc412cc65fc681576a9aee9c`.

Không xác nhận danh tính giọng/nhạc/SFX gốc hoặc tự nhận đã nghe bằng tai người, cũng không chứng nhận chất lượng giống hệt video mẫu. Preset 2D “Điện thoại gọi về quá khứ” giữ theo lựa chọn hiện hành; dự án 3D rác thành vàng vẫn dừng. Dự án cũ và installed skills được giữ nguyên; checksum MP4 điện thoại cũ đã xác minh. Không paid API, trọng số ngoài Git.

Thư mục: `/workspace/outputs/magic-eraser-2d-20261121`.
