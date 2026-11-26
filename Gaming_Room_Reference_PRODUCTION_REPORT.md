# Căn cứ gaming bí mật — nhân vật mẫu và nhịp kể nhanh

**File hoàn chỉnh:** `Can_Cu_Gaming_Bi_Mat_Nhan_Vat_Mau_Nhip_Nhanh_1080x1920.mp4` · **53.40 giây** · **1080×1920 ·30FPS** · 1602 khung hình.

## Thay đổi theo yêu cầu

- Dùng lại artwork gốc đã tách bộ phận của nhân vật trong hai demo người dùng gửi: mặt tròn, tóc đen, áo kem không tay, quần xanh, tay nhỏ gọn, giày sáng. Không dùng lại nhân vật áo khoác dài của bản trước. Mẹ có artwork riêng cùng ngôn ngữ hình ảnh.23xương cho mỗi nhân vật; không dùng ảnh toàn thân để giả hoạt hình.
- Hiệu chỉnh chiều dài chân/mesh theo mẫu và các vị trí tiếp xúc; giữ cùng một tỷ lệ X/Y, tránh kéo dãn toàn nhân vật. Góc rộng thấy dáng người, cận khi cần phản ứng hoặc vật thể; căn phòng ngủ, kho và phòng khách vẫn phân biệt rõ. Giữ chuyển động độc lập giữa nhân vật, bối cảnh, đạo cụ và camera/parallax.
- Bám nhịp ngắn của video “Biến đống rơm thành căn cứ”: liên kết nguy cơ–hành động–kết quả, phụ đề ngắn, hành động nối tiếp. Giữ đủ18 đoạn lời kể gốc và26 cảnh, không chèn intro/logo chờ. Bản mới trung bình **6.29 tiếng/giây** tính cả ngắt nghỉ; mục tiêu6,5 tiếng/giây ở phần có lời. Đây là số đếm token tiếng Việt phân cách bằng khoảng trắng theo WAV đã đo.
- Không tạo lạiTTS: dùng các segment VieNeu-TTS v3 Turbo đã có, chỉnh tốc độ giữ cao độ1,015625× và khoảng nối đoạn0,06–0,12giây cộng căn biên khung hình. Giọng yêu cầu Minh Quân hiện ánh xạ sang preset gốc Hải Đăng trong adapter cục bộ; model Apache-2.0, ONNXfp32 CPU, không cloud inference. Trọng số vẫn nằm ngoàiGit.
- Đồng bộ lại17 cueSFX Wyzowl CC0, nhạc và foley tổng hợp cục bộ theo timeline mới. Không sao chép nhạc, lời đọc hoặc hình của video tham khảo vào bản xuất.

## Kiểm tra thực tế

- MP4 giải mã toàn bộ thành công, đúng độ phân giải/FPS/số khung hình; không phát hiện đoạn đen theo bộ dò đã dùng.
- Trích26 ảnh trực tiếp từ MP4 để rà tư thế, nhân vật, bố cục và chữ; kiểm tra mẫu vùng an toàn phụ đề và tiếp xúc tay với tay nắm, thùng đồ, bàn và quạt.
- 2093 tư thế kiểm tra bằng rig thực: sai số chiều dài xương và đầuIK <0,001đơn vị,0 lần ép cổ tay vượt tầm với, cả hai gối hướng phía trước, khuỷu tay bê thùng hướng ra ngoài. Đường tay uống nước được chỉnh để tránh gập tay vào đúng gốc vai và đưa miệng chai tới miệng.
- Hai rig validate không lỗi; mở và phát MP4 trong Chromium ở đầu, đoạn thông gió và cuối, không lỗi phát trong các cửa sổ thử. Đây là kiểm tra phát kỹ thuật có tắt tiếng, không phải thẩm định bằng tai toàn bộ phim.
- AAC cuối: **-14.0 LUFS**, **-2.1 dBTP**,0 mẫu clipping; các cue khớp marker khung hình. Kiểm tra số học không bảo đảm cảm nhận thẩm mỹ/nghe chủ quan.

## Phạm vi đối chiếu

File tham khảo mới có SHA-256 trùng chính xác bản đã phân tích cục bộ: `2b47c5289cbed7b4416db2c033b44561b72e4f0230fd7601812a9a944ad36ca4`. Tái sử dụng phân tích153 ảnh mẫu/ASR local có sẵn để tiết kiệm công đoạn. Bản tham khảo38,22giây có khoảng16 nhịp sự kiện phân tích; đây không phải số cú cắt. Lời kể bản gaming khác và dài hơn, nên không khẳng định nhịp/giọng/từng khung hình giống100%. Giữ hướng nhịp nhanh của mẫu và tốc độ người dùng đã chọn.

Hình là2D/2.5D theo lớp, không phải render3D vật lý. Phụ đề được chia cụm tối đa5 token và căn theo thời lượng câu thực đo; chưa forced-align từng âm vị/từ. Các sơ đồ mặt cắt bổ trợ các cảnh nhân vật diễn xuất, không thay thế bằng slideshow.

## File

- MP4: `/workspace/outputs/gaming-secret-room-reference-20261126/final-reviewed/Can_Cu_Gaming_Bi_Mat_Nhan_Vat_Mau_Nhip_Nhanh_1080x1920.mp4`.
- SRT: `Can_Cu_Gaming_Bi_Mat_Nhan_Vat_Mau.vi.srt` trong bản tải GitHub.
- SHA-256 MP4: `94312ebbe4fe8b2ecdb6d6bfc0e6ae71e6300f545bd5f111246e93154c5076cf`.
- SHA-256 lời đọc làm việc: `03810cb45c04c095a624c82103f4c4a9a9654ad5c55080be100d3e98def97be1`.
- Dung lượng: 10,601,420byte, dưới giới hạn GitHub100MiB; không cần chia file hayGitLFS.
- Báo cáo kiểm tra, manifest và bằng chứng trong `/workspace/outputs/gaming-secret-room-reference-20261126/qa` và `/workspace/outputs/gaming-secret-room-reference-20261126/manifests`.

Giữ nguyên các video cũ và lời đọc cũ; bản này nằm ở thư mục mới. Không dùng API trả phí, GPU thuê, ảnhAI hay gói dịch vụ có phí.
