# CA ĐÊM 23:17 — bản phim rút nhịp

18 cảnh, 153 shot, 87 câu thoại tiếng Việt và 2 tin nhắn trên màn hình. Thời lượng 4 phút 20,792 giây, 1920×1080, 16:9, 24fps. Đây là bản rút nhịp theo yêu cầu của người dùng, không phải bản giữ timeline 28:18. Không bỏ câu thoại để rút thời lượng; các nhịp chờ và động tác im lặng được nén. Khoảng lặng thoại dài nhất đo theo RMS 10ms là 2,52 giây.

Mở `CaDem2317_Full_Vietnamese_1080p.mp4` bằng trình phát MP4; phụ đề tiếng Việt đã được ghi vào hình. File `.srt` đi kèm để chỉnh sửa. `index.html` là trang xem tại máy khi được phục vụ qua HTTP.

Hình ảnh hoạt hình vector 2D nhiều lớp / 2.5D mềm, với chuyển động tay chân IK, bước đi, tương tác đạo cụ và góc máy theo shot list. Không phải mô hình Blender 3D. VieNeu-TTS v3 Turbo chạy trên CPU cục bộ; nhạc và SFX tổng hợp tại máy. Xem CREDITS.md.

Kiểm tra: so sánh toàn bộ câu thoại với kịch bản; kiểm tra thời gian và khung hình từng cảnh; kiểm tra hình giữa của 153 shot; kiểm tra toán học độ dài xương ở các pha mẫu và trong render; giải mã toàn bộ MP4 bằng FFmpeg. Các kiểm tra tự động không thay thế việc nghe duyệt diễn xuất giọng và đánh giá thẩm mỹ bởi con người.

Không sửa các dự án Video Shotcraft có trước, không đưa model weights vào Git, không sử dụng API trả phí.
