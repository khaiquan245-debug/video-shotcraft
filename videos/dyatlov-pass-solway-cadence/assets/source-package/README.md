# 3 ảnh tư liệu thật — Dyatlov Pass (1959) — VideoShotCraft

**Trạng thái tại thời điểm đóng gói:** Tôi đã xác minh được trang nguồn và ảnh hiển thị trên web, nhưng môi trường tải file bị chặn, nên ZIP này CHƯA chứa ba tệp JPEG gốc. Không thay thế bằng ảnh AI.

## Ba ảnh được yêu cầu

1. `anh_that/01_nhom_nguoi_leo_nui_1959.jpg`: ảnh nhóm người đi bộ đường dài trước thảm kịch (nguồn DyatlovPass). URL ảnh: https://dyatlovpass.com/resources/340/gallery/Yuri-Doroshenko-13.jpg
2. `anh_that/02_anh_cuoi_chuan_bi_dung_leu_1959.jpg`: ảnh nhóm đào tuyết chuẩn bị dựng lều chiều 1/2/1959 (Figure 1a, ETH Zurich / Dyatlov Memorial Foundation). URL: https://geomechanics.ethz.ch/project-list/Dyatlov_pass/_jcr_content/par/image/image.imageformat.1286.965835515.jpg . *Figure 1 gồm 3 hình; script cắt phần a là bức ảnh cần dùng.*
3. `anh_that/03_leu_duoc_tim_thay_1959.jpg`: ảnh lều khi đội tìm kiếm phát hiện tháng 2/1959. URL: https://dyatlovpass.com/resources/340/Dyatlov-pass-tent-01.jpg . Bản khác: https://commons.wikimedia.org/wiki/File:Dyatlov_Pass_incident_02.jpg

## Tải thành ảnh thật

Khi chạy ở máy có Internet và có Python + Pillow:

```bash
pip install pillow
python download_images.py
```

Sau đó thư mục `anh_that/` sẽ có các ảnh .jpg, có thể đưa vào VideoShotCraft. Nếu tải tự động bị chặn, mở các URL ở trên, lưu thủ công theo đúng tên file.

**Chú ý:** Ảnh có thật không đồng nghĩa đã được cấp quyền đăng lại. Quyền tái sử dụng những ảnh này chưa được xác minh đầy đủ; liên hệ chủ sở hữu hoặc xác minh giấy phép trước khi xuất bản YouTube. Không dùng ảnh dựng AI để đánh tráo thành ảnh 1959.
