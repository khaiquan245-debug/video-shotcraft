# Đối chiếu nhịp kể và bản dựng FAST V2

Hai MP4 vừa gửi đã được đối chiếu SHA-256: video gốc cây trùng V1 đã xuất, video rơm trùng bản tham khảo đã phân tích. Nhận xét dựa trên khung hình theo thời gian, phụ đề trong hình, ASR local và đo audio. Không phải kết quả duyệt bằng tai người.

| Tiêu chí | Video tham khảo | Gốc cây V1 | FAST V2 |
|---|---|---|---|
| Thời lượng | 38,22 giây | 30 giây | 30 giây |
| Đơn vị tách theo khoảng trắng trong lời | 191, từ bản dựng lại lời | 89 | 154 |
| Mật độ lời trên toàn video | ≈5,00/giây | ≈2,97/giây | ≈5,13/giây |
| Khoảng yên lớn nhất trên track giọng, RMS < 0,003 | Không có track giọng riêng để đo tương đương | 2,86 giây | 0,28 giây |
| Cách phát triển | Nguy cơ → giải pháp → nguy cơ mới | Ít lời, chừa khoảng chờ hành động | Lời nối sát; thêm võng tuột → bắt dây → thắt nút → nhảy |

“Tiếng/giây” ở đây là phép đếm gần đúng theo khoảng trắng tiếng Việt, không phải phân tích âm tiết ngữ âm hay điểm chất lượng. Mốc ASR của video mẫu không đồng nhất với phép đo RMS trên track giọng tách riêng của V1/V2.

## Những gì đã sửa

- Giữ nhân vật, bối cảnh, câu chuyện gốc cây/thoát nước/ếch/võng và preset giọng cũ.
- Viết lại lời dẫn nối nhân quả theo “nhưng/thế là”, dùng câu ngắn có hành động tương ứng. Bản mới không chỉ là tăng tốc toàn bộ MP4 V1.
- Thu lại bằng VieNeu-TTS v3 Turbo local. Giọng native dài 39,46 giây; thu gọn khoảng yên ở biên câu, giữ đệm 40/45 ms, đổi khoảng nối 180 ms thành 40 ms. Không cắt lời bên trong câu.
- Sau ghép biên câu, audio dài 34,15 giây. FFmpeg `atempo=1.149057873485868` giữ cao độ, cho giọng cuối dài 29,722 giây. Tốc độ giọng tăng khoảng 14,9%; mật độ lời tăng còn do có thêm nội dung.
- Chỉnh tốc độ từng hành động và góc máy: cận búa/giày/xẻng/nút dây, trả về góc rộng cho cú nhảy. Mưa và vi chuyển động tiếp tục khi nhân vật thắt dây.
- Đặt lại SFX theo các tiếp xúc mới, thêm âm bật dây; nhạc pluck nguyên tác ở 120 BPM. Không dùng hình hoặc soundtrack của video mẫu trong bản mới.
- Phụ đề có 41 cụm nghĩa, căn theo thời gian từng câu sau xử lý tốc độ; mốc bên trong câu được ước lượng, chưa phải forced alignment từng từ.

## Kiểm tra tệp thực tế

MP4 dài 30,000 giây, 1080×1920, 30 fps, 900 khung hình; H.264/AAC stereo 48 kHz. Giải mã toàn bộ tệp thành công. Phát thử Chromium ở tốc độ 1× kết thúc đủ 30 giây, không báo lỗi video; phiên phát kiểm tra tắt tiếng.

Âm lượng đo được −14,2 LUFS, true peak −2,0 dBTP. Kiểm tra rig ở 3.600 mẫu tay/chân không có đích ngoài tầm. Đã xem ảnh trích từ MP4 ở các nhịp đóng búa, đào rãnh, võng tuột, thắt lại và nhảy lên.

Các phép kiểm tra này không bảo đảm mọi chuyển động đều đẹp hoặc không có mọi kiểu chồng lớp. Tạo hình và bàn tay 2D vẫn giản lược; không tự chứng nhận tương đương thẩm mỹ hoặc giọng của video tham khảo. Cần người xem duyệt thêm độ dễ nghe và cảm xúc.

## Bảo toàn và nguồn

V1 cùng các WAV đã có không bị ghi đè. WAV native mới có provenance và checksum riêng. Model chạy CPU local, trọng số nằm ngoài Git; không dùng API trả phí. Preset thực tế là Hải Đăng, được adapter hiện tại gọi bằng alias Minh Quân.

Trong gói tải: `Pacing_Comparison.png`, `Timeline_FAST_V2.csv`, `qa/final.json`, `qa/browser-playback.json`, `manifests/voice-fast.json` và ảnh trích kiểm tra.
