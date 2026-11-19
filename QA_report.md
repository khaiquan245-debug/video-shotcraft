# QA thực tế — Bận rộn nhưng không tiến bộ

## Kết quả

- MP4 master: `/workspace/video-shotcraft/busy_not_progressing/output/Busy_Not_Progressing_1080p.mp4`.
- Đã xuất **24/24 phân đoạn, 120/120 shot**, nguyên thứ tự JSON; CSV120 dòng trùng JSON.
- Thời lượng format **509.800s (8:29,8)**; video **15,293 frame**, 1920×1080,30fps,H.264/yuv420p; AAC stereo48kHz.
- Bitrate video thực đo: **7.983Mbps**; dung lượng **521,457,168byte**.
- Âm lượng: **-14.0LUFS**, true peak **-1.9dBFS**. Khoảng lời dẫn yên dài nhất (RMS10ms): **2.19s**, gồm kết phim chủ ý.
- SHA-256: `9ddc3c9ae60931fc1ec99a0e1d29fcb31653526ddf60b408a62d8418abf5cb3f`.
- Giải mã toàn bộ bằng FFmpeg đã qua; cả video và audio stream tồn tại.

## Nguồn và hình ảnh

Đã đọc đầy đủ nội dung văn bản, 24 đoạn kể, storyboard120 shot, JSON và CSV. Hai JPEG nhúng đã giải mã bằng code; SHA khớp dữ liệu nguồn: `thumbnail_style_mac_ket.jpg` và `thumbnail_style_tinh_di.jpg`. Đây là tài liệu tạo hình, không dùng làm frame nền cho phim. Bản gốc/ảnh/manifest đều được lưu trong project riêng; không sửa phim cũ hay skill đã cài.

Nhân vật Minh27 tuổi dùng chung rig/màu đầu/mắt/trang phục sơ mi trắng-xám và cà vạt navy. Các nhân vật phụ ởS23 có màu áo riêng. `characters/rig.mjs` có13 action tái sử dụng; có character master, background masters và ba poster gốc. Phim vẽ từng frame bằng vector nhiều lớp: nhân vật, vật thể, kiến trúc, ánh sáng và camera riêng. Không phải slideshow ảnh tĩnh; không dùng diffusion/videoAPI.

## Chuyển động và lượt sửa

- Đo với camera cố định, bỏ phụ đề: **120/120shot** có biến đổi pixel từ chủ thể/đạo cụ/giao diện (**100.0%**, yêu cầu≥70%). Đây là chỉ số chuyển động, không phải chấm điểm nghệ thuật.
- Bước đi2bước/giây; gõ phím4,2nhịp/giây (hai tay luân phiên); phản ứng bắt đầu0,17s, quay đầu0,33s; bấm/chạm0,32s với giữ đỉnh0,09s; ngồi/đứng0,85s. Hệ số1,5× là mục tiêu thiết kế; không tuyên bố đã đo tốc độ toàn bộ phim cũ để suy ra một tỷ lệ thực nghiệm.
- Chu kỳ bước đều: chân trụ cố định theo mặt đất/băng chuyền, sai số đo `1.42e-14`pixel thiết kế. Kiểm tra này không tự chứng minh mọi bước chuyển tư thế hoàn hảo.
- Toàn bộ frame render kiểm tra tầm với IK/chiều dài xương; không có pose vượt tầm với trong các checkpoint thành công. Chuyển động biểu cảm và đạo cụ vẫn mang tính cách điệu2D, không phải mô phỏng cơ thể/vải3D.
- Đã sửa lỗi font-weight750 làm tràn chữ, hướng gập gối khi ngồi, lớp cốc thiếu restore làm lệch phụ đề, điểm neo tay/nắm cửa và bố cục/đôi tay ở cảnh xe buýt. Có log/lượt lỗi lưu ở `qa/`; không dùng bản lỗi làm bản cuối.
- Demo12giây thật đã render/ffprobe/phát1×. Đoạn kỹ thuật30giây gồm bước đi/thao tác/phản ứng đã render và phát1×. Phim đầy đủ đã phát đến hết ở4× trong Chromium tắt tiếng, không lỗi phát.

## Lời kể, phụ đề và âm thanh

Một voice-over duy nhất: **Minh Đức — VieNeu-TTS v3 Turbo, ONNX CPU offline**, model revision61b85e3d937fbbacb387714180e8182823512523 (modelApache-2.0). Cả24đoạn giữ nguyên chữ nguồn; không thêm hội thoại, không nhép miệng. Không tua giọng; chỉ giảm phần đệm im lặng nhân tạo giữa chunk từ100ms xuống35ms, giữ WAV gốc riêng. Model weights ở `/workspace/tts-runtime/`, ngoài Git.

Mỗi cảnh hình dài17–23s; vài đoạn kể đi qua ranh giới hình bằngJ/L-cut, dịch tối đa khoảng1,67s, để giữ nguyên câu và đạt tổng8:30. Nhạc/SFX tạo mới bằng oscillator/noise/NumPy; có click, phím, báo, giấy, ghế, bước chân, cửa, cốc và nền quạt. Music duck15dB khi có lời;S17–S18 giảm sâu;S24 fade2s. SFX là bản tổng hợp cách điệu, không phải Foley thu thật. Nguồn khoa học ởYOUTUBE_DESCRIPTION.md; không thêm khẳng định tuyệt đối hoặc số liệu mới.

Phụ đề102cụm, tiếng Việt có dấu, nền/viền tối và vùng an toàn dưới khung. Timing dựa chunkTTS đo thực tế + điểm năng lượng thấp, **chưa phải forced alignment từng từ**.

## Phạm vi kiểm tra và giới hạn

Đã trích đủ6mốc yêu cầu:00:05,01:35,03:30,05:30,06:30,07:50; thêm cảnh xe buýt, đặt cốc và nắm cửa. Ảnh ở `qa/final-*.jpg`. Kiểm tra phát trình duyệt là kiểm tra kỹ thuật tắt tiếng; không tuyên bố đã nghe bằng tai, kiểm định giọng vùng miền hoặc được người dùng duyệt thẩm mỹ.

Thực thi trên Linux CPU (quota4core, hostRAM~33GiB), không cần GPU. Có launcher `render.ps1`, mặc định render tuần tự và checkpoint để phù hợp máy hạn chế VRAM; **chưa benchmark trên Windows/i5-6500/GTX1060 3GB thực tế**. Không dùngAPItrả phí. Không có lỗi cài đặt/model/mạng chặn sản xuất; có cảnh báo telemetryID không lưu được, SDK dùngID trongRAM và vẫn tạo đủ24WAV.
