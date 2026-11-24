# Pháo đài zombie — Máy phát hết nhiên liệu

MP4 **37,6giây**, **1080×1920**,30fps,1128frame. Có narration tiếng Việt, phụ đề, nhạc và SFX. Script và caption giữ nguyên218tiếng theo khoảng trắng; nhịp toàn phim **5.80tiếng/giây**, cùng hướng FAST V2.

## Không gian trong/ngoài

Nhà2tầng có sàn, cầu thang và tường bao cố định; kho ở sân thấp hơn. Cảnh trong phòng dùng mặt cắt sáng, zombie ngoài sân chỉ hiện qua ô cửa trong các shot cửa sổ. Cảnh nhìn ngoài dùng tường mặt ngoài; zombie trên mái và dưới sàn bị phá giữ vị trí riêng. Sân đi lại và móng cao tách rõ nền trong nhà/kho với lối ngoài. Cổng và hàng rào có từ đầu; khi đóng, nhân vật ở phía trong, đàn zombie tập trung ngoài chuông. CCTV ghi SÂN NGOÀI để giữ rõ hướng nhìn.

Có chạy vào nhà, kéo tủ, nâng ván, leo thang, đẩy giường, bám tay nắm trolley trượt sang kho, kéo dây khởi động máy, đặt mô-tơ và đóng cổng. Các nẹp cửa, tủ, giường và lỗ sàn giữ trạng thái qua các shot. Đây là phim hoạt hình hư cấu, có cắt thời gian để kể nhanh.

Giọng thực tế **VieNeu-TTS v3 Turbo**, ONNX CPU offline, preset **Hải Đăng** (alias Minh Quân). WAV native **54.56s** được giữ nguyên; bỏ khoảng yên thành **48.22s**, atempo **1.2964×** giữ cao độ, ra giọng **37.207s**. Nhấn âm lượng nhẹ ở các cụm đảo tình huống; không đổi speaker qua cảnh.

Âm thanh có **70cue**, nhạc Investigations và Foley có giấy phép, cùng lớp creature/mechanical/room-tone tự thiết kế. Chuông, máy phát, camera và màn hình dùng chung trạng thái nguồn; hết nhiên liệu thì máy/mô-tơ dừng và màn hình tối. Stock generic-engine-start là chất liệu máy đề được biên tập, không tự nhận là thu âm đúng chiếc máy phát đang vẽ. Nhạc cần ghi nguồn khi đăng: MUSIC_CREDIT.txt; các nguồn khác trong CREDITS.md.

QA thực tế: giải mã toàn MP4, đúng codec/kích thước/fps, **-14.1LUFS**, **-1.9dBTP**; khoảng yên giọng lớn nhất **0.37s**. Rig ghi **20468phép giải**, **0đích vượt tầm**, sai số xương tối đa **6.39e-14**. Đã xem draft và frame giải mã các cảnh trong/ngoài, dây trượt, cổng và kết. Chromium1× chạy hết file; playback này tắt tiếng, không phải duyệt bằng tai người. Caption chia cụm nghĩa trong các câu đã đo, chưa forced-align từng từ; không chạy ASR mặc định. Số đo xương không tự chứng nhận mọi tiếp xúc/che khuất hoặc diễn xuất hoàn hảo.

Không paid API/cloud inference; model weights ngoài Git. Các phim cũ và installed skills giữ nguyên. SHA-256: `89418f14b2a823f73892ccde0324d3f0b27dc1fab9369bbe50e621cc7b356933`.
Project local: `/workspace/outputs/zombie-house-fortress-20261124`.
