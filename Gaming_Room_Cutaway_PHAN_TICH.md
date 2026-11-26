# Phân tích tham khảo và cách dựng lại phòng gaming

Nguồn người dùng: “Biến đống rơm thành căn cứ”,38,22giây,1080×1920,30FPS. SHA-256`2b47c5289cbed7b4416db2c033b44561b72e4f0230fd7601812a9a944ad36ca4`, trùng chính xác bản đã phân tích cục bộ bằng153 ảnh mẫu và ASR CPU. Tái sử dụng đúng phân tích này để tránh chạy lại công đoạn không cần thiết. Không đưa hình/nhạc/lời đọc của video tham khảo vào bản xuất.

## Điều tạo nên nhịp kể của mẫu

Mẫu kể theo chuỗi **nguy cơ → thao tác → kết quả → vấn đề mới**. Mỗi động từ làm thay đổi một vật thể cụ thể. Ván gỗ tạo thành hộp; ống tre nối lên đỉnh; cú đào mở thêm khoảng rỗng; đường hầm dẫn sang chuồng lợn. Camera cho thấy kết quả trước khi chuyển sang trở ngại tiếp theo. Nhịp nhanh đến từ lượng sự việc và quan hệ nhân–quả rõ ràng.

Khoảng16 nhịp sự kiện được phân tích trên38,22giây, đa số1,5–3,5giây. Đây là phân chia nội dung, **không phải số cú cắt**. Các cụm phụ đề đổi nhanh, khoảng0,5–1giây ở nhiều đoạn; camera có thể đi qua nhiều cụm phụ đề trong một chuyển động. ASR local cho khoảng191 token tiếng Việt trên toàn file, xấp xỉ5tiếng/giây; nhận dạng có lỗi nên không coi đây là đo phát âm tuyệt đối. Người dùng đã chọn nhịp đọc nhanh6–6,5tiếng/giây cho phim gaming; bản dựng giữ giọng đã duyệt, trung bình6,29tiếng/giây tính cả khoảng nghỉ.

## Bối cảnh và camera

Mẫu dùng một bản đồ ổn định: mặt đất, đống rơm, nhà lính, trạm gác, chuồng lợn và hầm bên dưới. Các nâng cấp trước vẫn tồn tại ở cảnh sau. Người xem nhớ được vị trí và nhận ra sự tiến triển. Cỡ cảnh thay đổi để giải thích nguyên nhân: cận mặt khi ngạt, bám theo ống tre để hiểu luồng khí, hạ xuống khi đào, lia theo đường hầm, kéo rộng cuối để thấy toàn căn cứ. MP4 không cho phép xác nhận phần mềm gốc hay loại rig tác giả đã dùng.

| Tham khảo | Áp dụng vào bản dựng mới |
|---|---|
| Bản đồ mặt đất–hầm liên tục | Mặt cắt chung phòng ngủ–kho sau tủ–phòng khách; chung sàn, tường và lối đi |
| Công trình tăng dần sau mỗi thao tác | Thùng cũ giảm đi, sàn sạch, bàn/PC lắp vào, đèn sáng, kệ và vật dụng xuất hiện sau khi làm |
| Camera theo ống tre và đường đào | Camera bám tay kéo tủ, đẩy bàn, mở rộng theo đường ống thông gió, lia theo sóng âm sang mẹ |
| Cận nguồn nguy hiểm rồi phản ứng | Nhiệt đi từPC lên mặt; camera vào màn hình thật khi mất mạng, rồi trả về người kiểm tra |
| Những phần đã xây vẫn còn | Quạt, ống, kệ và cách âm được giữ ở những cảnh sau, không biến mất khi đổi góc |
| Payoff kéo rộng cả hệ thống | Căn phòng gaming hiện đủ đồ, rồi chuyển thành phòng học ngay trong cùng căn phòng |

## Phần được làm lại

Bản trước có nhiều đồ đặt sẵn trước lời kể; phòng kho là các mảng nền lặp, camera thường đổi cỡ trên cùng bố cục. Bản mới dùng một ngôi nhà cắt lớp được vẽ lại bằng code: tường, trần, cửa, lớp sàn/dầm, móng/đất và ba phòng có vị trí cố định. Không dùng các ảnh phòng tĩnh để zoom.

Đạo cụ có trạng thái theo timeline: chưa lắp, đang cầm/di chuyển, đã đặt, bật/tắt, tháo dọn hoặc đổi công năng. Các điểm kéo tủ, đẩy bàn, nhấn công tắc, lắp quạt và đặt tấm cách âm dùng tọa độ tay từ rig. Ống thông gió nằm ở lớp dịch vụ phía sau đồ đạc và đi sát tường/trần, không cắt ngang chữ trên màn hình. Bảng báo lỗi toàn màn hình được bỏ; cảnh cận dùng đúng màn hìnhPC trong căn phòng.

Nhân vật áo kem/quần xanh và rig23xương được giữ. Có chuyển động chân, hông, vai, khuỷu, tay, cổ, đầu, mắt và miệng; cả hai gối hướng về trước, khuỷu bê thùng mở ra ngoài. Dùng cận, trung, toàn, tracking, pan, reveal và pull-back theo mục đích. Đây là hoạt hình2D cắt lớp và camera phẳng có parallax; không tuyên bố góc quay3D vật lý.

Phụ đề đổi sang chữ hoa trắng, viền đậm, một dòng và tối đa4token/cụm; tránh tách các từ ghép như “bí mật”, “máy tính”, “phòng khách”, “kết nối”. Thời lượng câu lấy từ WAV đã đo; chưa forced-align từng từ/âm vị. SFX chọn từ WyzowlCC0 và đặt theo frame thao tác; nhạc/foley gốc được tổng hợp cục bộ, không dùng API trả phí.

Các nhận xét về nhịp/không gian dựa trên ảnh theo thời gian, source động tác, metadata và ASR local. Không tuyên bố nghe bằng tai toàn bộ nhạc/giọng tham khảo hoặc tái tạo giống100% từng khung hình. Bản mới áp dụng cấu trúc dựng này cho một kịch bản khác, dài53,4giây.
