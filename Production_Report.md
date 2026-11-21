# Kết quả thực tế — Máy bán hàng biết trước tương lai

MP4 **25.300 giây**, **1080×1920**, **30 fps**, **759 frame**, H.264 yuv420p/AAC stereo 48 kHz, **4,109,240 byte**. Đầu vào và phụ đề giữ nguyên 134 tiếng tách theo khoảng trắng và thứ tự kịch bản.

## Nhịp nhanh hơn

Nhịp lời toàn phim **5.296 tiếng/giây**, tăng **5.9%** từ mức 5,0 của phim cục tẩy. WAV native **33.600 giây** được giữ nguyên, cắt yên ở biên câu thành **29.100 giây**, rồi FFmpeg atempo **1.169002×**, giữ cao độ, cho giọng **24.906 giây**. Khoảng yên dài nhất trên stem giọng kể gồm đuôi phim **0.57 giây**. Không thêm lời hoặc đoạn chờ để kéo thời lượng.

## Hình và diễn hoạt

Một nhân vật áo cam, một chó con sống, cùng thiết kế máy/chìa/ảnh/đồng xu qua các shot. Ảnh giấy chứa hình tương lai của cùng nhân vật ôm chó trước nhà kho và biển rơi; ảnh trong tay dùng đúng một asset in cố định. Các insert ảnh/đồng xu là góc cận đạo cụ trong phim có diễn hoạt, không thay toàn phim bằng ảnh tĩnh.

Có đi, bỏ xu, máy nhả đồ, cúi nhận chìa/ảnh, cầm chìa xoay đúng lỗ khóa, cửa mở theo bản lề bên phải, đẩy ván chặn rồi nhấc chó, nhìn lại ảnh, lấy đà và nhảy sang trái. Chó giữ bên tay còn lại khi người đàn ông xem ảnh hoặc nhặt xu. Macro ảnh không thêm bàn tay đang bận ôm chó. Biển rơi sau khi nhân vật ra khỏi vùng va chạm; nền/cửa/biển/ván còn lại được giữ trạng thái. Khi quay lại vị trí cũ, máy đã mất, chỉ còn đồng xu. Dòng khắc và phụ đề kết cùng hiện rõ.

Tay/chân dùng IK hai đoạn cố định. Render final: **2356 phép giải**, **0 đích ngoài tầm**, sai số chiều dài xương tối đa **1.56e-13**. Đã xem draft và ảnh giải mã các tiếp xúc chính; các tọa độ giao nhận ghi trong qa/continuity.json. Đây là diễn hoạt hoạt hình, không chứng nhận vật lý/che khuất hoàn hảo ở mọi frame.

## Âm thanh, chữ và QA

Model thực tế **VieNeu-TTS v3 Turbo**, **ONNX CPU offline**, preset **Hải Đăng** (alias **Minh Quân**). **46 cụm phụ đề** một dòng, Nunito, theo biên câu đã đo và biên cụm nghĩa ước lượng; chưa forced-align từng từ.

Có nhạc nguyên tác 138 BPM, ambience và **36 cue SFX**, gồm coin/paper/key/door/wood-impact CC0 với item credits, các lớp accent và bước chân tự tạo. Master đo được **-14.2 LUFS**, **-2.1 dBTP**. Giải mã toàn MP4 thành công, kiểm tra đúng kích thước/fps/số frame. Chromium phát 1× đến cuối, SHA khớp file final; phiên playback kỹ thuật tắt tiếng.

ASR local faster-whisper-small có token similarity **87.3%** với script, lưu đầy đủ sai khác; nhận dạng tiếng Việt có lỗi âm/dấu, nên không coi mọi sai khác là lỗi phát âm TTS. Chưa có duyệt bằng tai người hoặc kiểm tra loa/tai nghe; không tự tuyên bố âm thanh/nhịp dừng giống hệt mẫu. Thẩm mỹ và diễn xuất không được chứng nhận chỉ bằng kiểm tra kỹ thuật.

Các file cũ/installed skills giữ nguyên; MP4 cục tẩy cũ đã xác minh checksum không đổi. Không paid API. Không weights trong Git. Chỉ xuất bản bản tải lên nhánh mới, không thay main.

MP4 SHA-256: `8fbd0db5ac261efbf53d8949b75ad0e6a47c60909a96edcd4a34a9b038943aa2`.
Project local: `/workspace/outputs/future-vending-machine-20261121`.
