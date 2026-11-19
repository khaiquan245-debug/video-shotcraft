# Bản sửa P0/P1 — Người bận rộn nhưng không tiến bộ

## Kết quả có thật
- Video: `Busy_Not_Progressing_P0P1_V2_1080p.mp4`; 509.800 giây; 1920×1080, 30 fps, H.264/yuv420p + AAC stereo48 kHz.
- Đã render 24 phân đoạn, 120 shot, 15293frame. Mã hóa cuối CRF 17 VBR để giảm dung lượng, giữ đủ nội dung và độ phân giải. Đây là hoạt hình vector có rig và đồ vật riêng; không phải ảnh tham chiếu phóng to/slideshow.
- Lời kể PCM gốc giữ nguyên từng byte, một giọng Minh Đức/VieNeu-TTS v3 Turbo ONNX CPU từ bản hiện tại; không đổi sang giọng khác, không tăng tốc VO. SHA256: `9c991ebad69a0f9b9c90990535d493231093e9c4c4dddb3dfe851152068368f3`.
- Nhạc/SFX mới được tổng hợp local bằng oscillator/noise; không dùng nhạc thương mại, API trả phí hay cloud inference.
- Loudness thực tế: -14.0LUFS; peak -2.1dBTP. Khoảng yên tối đa trong VO theo ngưỡngRMS: 2.19s.
- FFmpeg giải mã toàn bộ tệp thành công. Rig không có đích IK ngoài tầm trong các frame đã render; xem `qa/final.json`. Con số này không chứng minh diễn xuất hay hoặc không xuyên vật thể ở mọi pixel. Đã sửa tay đi bộ hạ xuống tự nhiên hơn và gắn bước chân khi mang giấy với vận tốc tịnh tiến; kiểm tra chân trụ riêng lưu ở `qa/footing.json`.
- Bản cũ được giữ nguyên trong `busy_not_progressing/`; bản sửa ở thư mục mới `busy_not_progressing_v2/`.

## Giới hạn nghiệm thu
Đây là bản sửa hoạt hình 2D đã render, không tự chấm đạt toàn bộ P1. Diễn xuất, bàn tay và góc nghiêng vẫn giản lược; không có xoay camera 3D thực, chưa căn phụ đề từng từ và chưa duyệt cảm xúc âm thanh bằng tai. Cảnh công việc vẫn cần một số bàn/laptop, nhưng đã giảm các poster UI toàn màn hình.

## P0 trước, rồi P1
| Ưu tiên | Thay đổi thực tế | Bằng chứng / giới hạn |
|---|---|---|
|P0 lặp cảnh|Tách nền nhà đêm, góc học, văn phòng sáng nhiều người, phố, xe buýt, café, giường, gia đình, hành lang và studio.|120 ảnh bố cục trong `qa/V2-*.jpg`; vẫn có motif bàn máy tính vì nội dung công việc, không tuyên bố đã bỏ toàn bộ.|
|P0 diễn xuất|Thêm xoa trán, bóp cổ, thả vai/tay, khép laptop, đẩy cốc, đi bộ, trao brief, nhấc/lật/đặt giấy, chạm/xoay tay nắm.|Các khớp được giải IK cố định chiều dài. Tay là hình bàn tay đơn giản, không phải bàn tay giải phẫu có từng ngón rig riêng.|
|P0 mất cơ hội|S14café/brief → S15ba bản nháp/ngập ngừng GỬI → S16người khác nhận poster sau kính và tin dự án đã có người làm.|Demo 04:45–05:05 và demo mất cơ hội. Đã sửa crop điện thoại sau lần kiểm tra đầu.|
|P0 cao trào|S17sau lưng tiến gần, vai gục, bàn tay mở, xoa trán rồi buông; S18chần chừ trước bản nháp.|Không dùng UI0% trong S17–S18. Shot khoảng5.7–7.6 giây, động tác được chia theo giai đoạn.|
|P1 nhịp|Mở đầu10 shot / 18 giây; xen cận/chi tiết/góc rộng ở phần giữa, giữ VO; tâm lý dài hơn.|Giữ tổng thời lượng8:29.8 để không đổi lời kể; không phải tua nhanh toàn phim. Chưa có microcut0.7–1.2 giây xuyên mọi montage.|
|P1 góc máy|CU/ECU tay–mắt, OTS/BACK, top-down, side/profile, tracking và push-in.|Là hoạt hình2D vector; góc nghiêng giản lược, không phải xoay camera3D quanh nhân vật.|
|P1 phụ đề|Tăng chữ36–42đơn vị thiết kế (54–63px ở1080p), đo chiều rộng để xuống dòng; kiểm tra frame360 px.|Nội dung/timing gốc giữ nguyên. Canh theo cụm nghĩa/chunk TTS và năng lượng, chưa phải forced alignment từng từ.|
|P1 âm thanh|Nhạc duck 15 dB khi có VO; giảm gần im ởS17/S18; giảm click lặp, SFX gắn mốc chạm.|Đo kỹ thuật và phát thử trình duyệt đã thực hiện. **Chưa thẩm định bằng tai người ở1×**, không đánh dấu yêu cầu này đạt.|
|P1 tiến bộ/kết|So sánh bản1/bản2; ba poster khác nhau; tay xoay cửa, bước qua ngưỡng và cắt sang studio sáng thật.|XemS20–S24 và ảnh trước–sau. Không chỉ đổi màu cánh cửa.|

## Demo và QA hình ảnh
- `Demo_Mo_Dau_15s.mp4`:15giây đầu.
- `Demo_Co_Hoi_04m45_20s.mp4`:04:45–05:05trên timeline.
- `Demo_Mat_Co_Hoi_20s.mp4`:20giây quanh việc nhận poster/tin mất cơ hội.
- `Demo_Cao_Trao_18s.mp4`:vai gục, tay mở, xoa trán.
- Mỗi demo có thư mục `qa/<ten_demo>_1fps/` và contact sheet, trích từ MP4 đã encode.
- `Before_After.jpg`:đối chiếu15mốc. Mở đầu nhanh hơn; buổi sáng/văn phòng khác ánh đêm; phần giữa xen thao tác/ngoại cảnh; café có quầy máy pha, bàn, đèn; cao trào bỏ0%; cuối bước sang studio.
- Đã sửa trong quá trình kiểm tra:lỗi audio block không chia hết480sample, crop camera gây mép đen, titlebrief trùng chữ, cốc trùng, khép laptop không chạy, crop mất phần trên tin nhắn, cảnh bản nháp chỉ giữ một tờ.

## Giới hạn nghiệm thu
Đây là bản sửa đã xuất đầy đủ, không phải tuyên bố đạt chất lượng điện ảnh cao cấp ở mọi shot. Một số động tác nhỏ và gương mặt vẫn theo rig vector tối giản; một vài insert giấy/màn hình còn cần người xem đánh giá độ cuốn hút. Chưa xác nhận bằng tai cảm xúc TTS/nhạc và chưa đối chiếu lời–hình tới từng từ. Việc phát trình duyệt tắt tiếng chỉ xác nhận tệp chơi được. Số shot và số pixel thay đổi không được dùng thay cho đánh giá kể chuyện.

## Chạy lại miễn phí
Python3 + NumPy/Pillow, Node + @napi-rs/canvas, FFmpeg. FontNunito giữ kèmOFL.
1.`python production/catalog.py` (tạoshotlist; không sửa thoại).
2.`python production/audio.py` (dùng lại audio/voice-full.wav, không TTS lại).
3.`node production/render.mjs --preflight`.
4.`node production/render.mjs --range 1 24` (checkpoint theo hash nguồn).
5.`python production/assemble.py` rồi `python production/report.py`.
Không cầnGPU trả phí. Trọng sốTTS ở ngoàiGit, không đóng trong gói video.
