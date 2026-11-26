# Bản dựng lại toàn bộ bối cảnh và camera — phòng gaming

**Video hoàn chỉnh:** `Can_Cu_Gaming_Bi_Mat_Dung_Lai_Boi_Canh_Goc_May_1080x1920.mp4` · **53.40 giây** · **1080×1920 ·30FPS** · 1602 khung hình · 13,584,318byte.

Đây là bản dựng phần hình mới toàn bộ: một mặt cắt ngôi nhà cố định với phòng ngủ, kho sau tủ và phòng khách. Tường, trần, cửa, sàn/dầm, móng/đất và nội thất được vẽ mới bằng code. Giữ nhân vật áo kem/quần xanh và lời kể đã duyệt, không sửa video cũ. Có phân tích tham khảo và bảng thay đổi trong `PHAN_TICH_VA_CACH_DUNG_LAI.md`.

## Thay đổi cụ thể

- Camera bám vị trí tay kéo tủ, theo bàn đang được đẩy, theo đường ống lên trần, lia theo sóng âm sang phòng khách và kéo rộng cho thấy kết quả nâng cấp.
- Không đặt sẵn toàn bộ đồ gaming trong kho. Thùng cũ giảm đi; sàn sạch; bàn,PC,đèn,kệ,quạt và cách âm xuất hiện theo bước thực hiện. Các phần đã xây vẫn giữ nguyên khi đổi góc.
- Camera báo mất mạng tiến vào đúng màn hìnhPC trong không gian thật; bỏ bảngUI phủ toàn khung hình. Đường ống dịch vụ nằm sau đồ đạc và sát tường/trần, không cắt ngang màn hình.
- Điểm kéo tủ/đẩy bàn/công tắc/quạt/tấm cách âm lấy từ xương bàn tay của nhân vật. Nhân vật diễn xuất bằng các bộ phận độc lập, có bước chân, gập hông/gối, bê, kéo, lắp, chơi game, phản ứng và dọn đồ.
- Phụ đề chữ hoa trắng, viền đậm, một dòng, cụm tối đa4token có bảo vệ một số từ ghép. Giữ53,4giây lời kể gốc của bản đã duyệt: trung bình6,29tiếng/giây tính cả khoảng nghỉ; không chạyTTS lại.
-18 cueSFX WyzowlCC0 đặt lại theo frame tiếp xúc/kích hoạt. Nhạc/foley gốc được tổng hợp cục bộ và dùng lại đúng quyền sử dụng; không lấy soundtrack từ tham khảo.

## Kiểm tra đã chạy trên sản phẩm

- Giải mã toàn bộ MP4, kích thước1080×1920,30FPS,1602frames; không có lỗi giải mã hoặc đoạn đen theo bộ dò.
- Trích và xem26 ảnh trực tiếp từ MP4, kiểm tra khớp, các thao tác và bố cục. Các ảnh nằm trong`qa/encoded` và bản tổng hợp`qa/encoded-contact-sheet.jpg`.
- 2639 tư thế Rigby: chiều dài xương và đầuIK sai số <0,001 đơn vị,0 lần ép cổ tay vượt tầm, cả hai gối hướng trước, khuỷu bê thùng mở ra ngoài. Kiểm tra này không tự chứng nhận mỹ thuật hay tự hiểu mọi hành động.
- Kiểm tra trạng thái xây dựng theo thời gian, sự tồn tại của các nâng cấp ở các cảnh sau, vị trí tiếp xúc đã chọn và vùng an toàn phụ đề. Phụ đề căn theo thời lượng câu đã đo, chưa forced-align từng từ/âm vị.
- Chromium phát MP4 thật ở đầu, đoạn thông gió và cuối, không lỗi trong các cửa sổ thử. Đây là phát kỹ thuật có tắt tiếng, không phải thẩm định bằng tai toàn bộ phim.
- AAC cuối đạt **-14.0LUFS**, **-2.1dBTP**,0 mẫu clipping. Kiểm tra cue dựa trên marker được tác giả đặt; không tự nhận biết tiếp xúc bằng thị giác hoặc bảo đảm cảm nhận nghe chủ quan.

## Nguồn và giới hạn

Lời kể tạo từ VieNeu-TTS v3 Turbo ONNXfp32 cục bộ, model Apache-2.0; tên Minh Quân trong adapter hiện ánh xạ tới preset gốc Hải Đăng. Trọng số vẫn nằm ngoàiGit. SHA-256 lời đọc giữ nguyên: `03810cb45c04c095a624c82103f4c4a9a9654ad5c55080be100d3e98def97be1`. Không cloud inference hoặc API trả phí.

Hình là hoạt hình2D cắt lớp/native Rigby23xương; có nhiều cỡ cảnh, camera pan/tracking/reveal và parallax, không phải góc quay3D vật lý. Áp dụng cách tổ chức không gian, quan hệ nhân–quả và nhịp của mẫu cho kịch bản gaming khác; không tuyên bố sao chép100% từng frame hoặc cùng giọng/nhạc với mẫu.

MP4 cục bộ: `/workspace/outputs/gaming-secret-room-cutaway-20261126/final/Can_Cu_Gaming_Bi_Mat_Dung_Lai_Boi_Canh_Goc_May_1080x1920.mp4`.
SHA-256 MP4: `9d23a5c8ede56f893540889f3f0d44221076655605c02c38b7c231b3b1f8feac`.
File dưới giới hạn GitHub100MiB; không chia nhỏ, khôngGitLFS. Không đưa trọng sốTTS hoặc video tham khảo vào GitHub. Các phiên bản cũ và narration gốc được giữ nguyên.
