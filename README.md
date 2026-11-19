# Bản đầy đủ — MASTER nguyên chất lượng

**[TẢI TOÀN BỘ BẰNG MỘT FILE ZIP](https://github.com/khaiquan245-debug/video-shotcraft/archive/refs/heads/downloads/busy-master-20261119.zip)** (khoảng229MB).

## Windows

1. Tải ZIP bằng liên kết trên, rồi **giải nén toàn bộ** vào một thư mục.
2. Mở thư mục vừa giải nén và nhấp đúp **`GHEP_VIDEO.cmd`**.
3. Chờ ghép/giải nén/xác minh. Script mở thư mục **`Video_Master`** chứa **`Busy_Not_Progressing_1080p.mp4`**.

Không cần cài Python hoặc tải riêng từng phần. Script chỉ đọc file trong gói, ghép ZIP, xác minh SHA-256, giải nén vào thư mục mới và mở thư mục kết quả; không cần quyền admin, không đổi chính sách PowerShell, không gọi mạng. Nếu có lỗi, cửa sổ giữ lại thông báo.

Mac/Linux hoặc người đã có Python3.8+: `python join_master.py` trong thư mục đã giải nén. Script Windows chưa được chạy trên máy Windows trong phiên này; quy trình ghép/giải nén và đối chiếu dữ liệu được kiểm tra bằng Python trên Linux.

## Nội dung thực tế

- Nguyên bản **24 phân đoạn,120shot**, dài **8:29,8**.
- **1920×1080,30fps,H.264**, video thực đo **7,983Mbps** (mục tiêu8Mbps), AAC.
- MP4 sau giải nén: **521.457.168byte**, SHA-256 **`9ddc3c9ae60931fc1ec99a0e1d29fcb31653526ddf60b408a62d8418abf5cb3f`**.
- ZIP chia ba phần dưới100MiB/file để lưu trên GitHub. Đây là nén/ghép file giữ nguyên dữ liệu, không mã hóa lại video.
- GitHub LFS đã từ chối tải đối tượng mới vào fork công khai này; gói chia phần khắc phục giới hạn bằng các file Git thông thường. Master được lưu đầy đủ trong ba phần.
- Đọc `QA_report.md` cho kết quả sản xuất. Bản tải nhẹ ở nhánh `downloads/busy-not-progressing-20261119` là phiên bản riêng.

Nhánh tải này không thay đổi main hoặc các dự án Video Shotcraft. Không API trả phí, không model weights trong Git.
