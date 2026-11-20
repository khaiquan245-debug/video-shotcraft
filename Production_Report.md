# Kết quả sản xuất thực tế

**Bạn tỉnh dậy trong tô ngũ cốc — 40 giây, 9:16.** Toàn bộ 154 đơn vị lời tách theo khoảng trắng của kịch bản được giữ đúng thứ tự trong nguồn TTS và chuỗi phụ đề. Tệp MP4 thật tồn tại, có hình và tiếng. Đây là hoạt hình vector 2D với khớp nhân vật và vật thể chuyển động, không phải slideshow ảnh tĩnh.

## Hình và dựng

18 khối hành động theo lời kể: ngoi lên → ôm ngũ cốc → thìa hất lên → mèo tới/thò chân → nhảy/trượt hộp → hộp đổ/ngũ cốc cuốn đi → chộp dây → ngũ cốc và mèo xuống sàn → đu lên cửa sổ → nhà nhỏ → mở cửa/nội thất → tô ngũ cốc → người dưới mặt sữa gõ. Đây là số khối kể, không phải đếm hard cut.

Nhân vật áo cam, tóc nâu đen, quần xanh và giày vàng được giữ từ FAST V2. Tay/chân dùng chuỗi hai xương có chiều dài cố định. Tô, thìa, mèo, hộp, rèm, nhà và căn phòng là hình vẽ mới; camera bám hành động, có các lớp nền/tiền cảnh riêng.

Đã sửa sau khi xem bản nháp: phụ đề quá dài được tách cụm nghĩa; tăng độ với tay hợp lý ở dây; hạ tư thế đi trong nhà để không duỗi chân quá tầm; sửa tô đặt đúng trên bàn; chỉnh tay gõ chạm thành; giữ ngũ cốc và mèo trên mặt sàn khi rơi xong; chỉnh hộp nằm xuống đúng mặt bàn và tư thế lăn không xuyên bàn; dời cú mèo nhảy lên bàn 1,3 giây để sát câu kể. Căn nhà được rèm che trước cảnh hé lộ.

## Giọng, phụ đề và âm thanh

Model thực tế: **VieNeu-TTS v3 Turbo**, backend **onnx**, CPU offline. Giọng thực tế **Hải Đăng**; tên Minh Quân trong adapter là alias của preset này. Native **37.60 giây**, tốc độ giữ 1,0×, không cắt hoặc kéo dài lời. Các WAV đã được duyệt ở dự án cũ không bị ghi đè.

43 cụm phụ đề một dòng. Mốc câu được đo từ từng đoạn TTS; mốc cụm bên trong câu được ước lượng theo số tiếng, chưa forced-align từng từ. ASR local được chạy như chẩn đoán bổ sung; bản nhận dạng có nhiều sai khác chính tả, không dùng nó thay lời gốc hoặc phụ đề. Chưa xác nhận phát âm từng từ bằng tai người.

91 sự kiện Foley trong spotting list, gồm các va chạm nhỏ của từng viên ngũ cốc. Âm thanh tự tổng hợp, không lấy soundtrack của mẫu. Nhạc nguyên tác nhanh ở phần thoát hiểm, ấm tại căn nhà; chủ đích bỏ nhạc từ 35,55 giây để ba tiếng gõ có không gian. Ba nhịp gõ hình/tiếng đặt tại 36,72/37,22/37,72 giây.

## Kiểm tra tệp

- Thời lượng **40.000 giây**; **1080×1920**, **30 fps**, **1200 khung hình**.
- H.264 yuv420p và AAC stereo 48 kHz; giải mã toàn bộ thành công.
- Âm lượng **-14.2 LUFS**, true peak **-1.8 dBTP**.
- Khoảng yên dài nhất trên track giọng theo RMS<0,003: **2.45 giây**, gồm đoạn kết chủ đích.
- Kiểm tra rig trong bản render: **6959 mẫu**, **0 đích ngoài tầm**, sai số chiều dài xương tối đa **1.71e-13**.
- Dung lượng **16895355 bytes**; SHA-256 `83290cc47cebd94ceb461f8e1988c0041bd2f19bcad51e4a8f98821de1088aa3`.

Ảnh kiểm tra được trích lại từ MP4 đã encode; log giải mã, loudness và phát trình duyệt được giữ trong QA. Phát trình duyệt 1× là kiểm tra kỹ thuật, tắt tiếng; không thay cho người xem duyệt cảm xúc/độ dễ nghe. Các phép đo khớp không bảo đảm mọi kiểu che khuất hay diễn xuất đều hoàn hảo. Mẫu mới chưa được người dùng duyệt.

Các nguồn và công cụ có sẵn đều chạy local: VieNeu-TTS/ONNX, Canvas, FFmpeg và ASR CPU. Không cần tải model mới, không phát sinh API trả phí. Trọng số model nằm ngoài Git. Thư mục dự án mới: `/workspace/outputs/cereal-wakeup-20261120`.
