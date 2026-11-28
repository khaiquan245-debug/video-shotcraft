# Báo cáo QA — Lời nói dối của mẹ

Bản MP4 giải mã đủ 1.516/1.516 khung ở 1080 × 1920, 30 FPS, 50,533 giây. H.264 và AAC 48 kHz stereo.

Đã xem contact sheet của 24 shot và các khung trước/sau bảy mốc thay đổi ảnh được báo. Cả bảy mốc rơi trùng lúc cụm phụ đề biến mất. Kiểm tra tự động không ghi nhận khung đen, trắng bất thường hay giữ nguyên từ 12 khung trở lên.

# Lời nói dối của mẹ — phạm vi kiểm tra bản ghép

- 7 địa điểm, 24 shot, 1.516 khung mục tiêu. Sáu địa điểm đầu lấy từ bản V3 render 1080 × 1920. Căn bếp là bản V4 được render lại theo lời kể, có cảnh chia thức ăn.
- Lời kể và chín âm báo tiền thuộc bản phối đã duyệt. Wyzowl bổ sung bảy mốc foley, gồm một hiệu ứng tắt điện thoại ngoài khung hình. Kịch bản, thời gian phát âm và cụm phụ đề gốc được tái sử dụng.
- Kiểm tra kỹ thuật đọc file bằng FFmpeg, đo số khung và mức âm thanh, đánh dấu khung màu đen, trắng và đoạn ít chuyển động. Kiểm tra số học không tự chứng minh cảm nhận chiều sâu, việc bàn tay nắm vật, hay từng mẫu âm thanh khớp tuyệt đối với hình.
- Nhân vật giữ nét vẽ 2D theo từng bộ phận, hiển thị trong không gian 3D. Tương tác tay nắm tủ có quỹ đạo tay 3D được soạn cho cảnh này. Các động tác còn lại dùng pose và mốc dựng riêng. Chưa có khóa chân vật lý, biến dạng mesh hoặc tự động dò va chạm toàn thân cho toàn bộ phim. Nhân vật phụ có chuyển động chọn lọc, không phải một hệ mô phỏng đám đông.
- Bộ QA tham chiếu của RicksClips được chạy trên file mã hóa. Three.js và pmndrs postprocessing phục vụ khung 3D, ACES và DOF/bloom ở một số shot. Riêng bếp V4 dùng normal map tự tạo và lớp tối tiếp xúc dưới nội thất. GLB/GLTF Kenney và KayKit dùng CC0. Không có API trả phí.
- Skill chính: cinematic-3d-world-camera-director. Các skill PixiJS Environment Director và Rigby2D được đọc, và hai bộ kiểm thử sẵn có đã chạy. Renderer của phim dùng Three.js và tạo pose vẽ trực tiếp trong texture, không dùng Rigby2D để kết xuất từng khung của phim. Wyzowl SFX Director thực hiện phối và QC âm thanh.

## Kết quả chạy QC ảnh

```text
SPECS 1080x1920 30/1 fps, 1516 frames, 50.533 s; audio: aac 48000 Hz 2ch
LOUDNESS I:         -14.0 LUFS | LRA:         1.5 LU | Peak:       -2.0 dBFS
SILENCES silence_start: 41.072292; silence_end: 41.529688 | silence_duration: 0.457396; silence_start: 48.014937; silence_end: 48.358 | silence_duration: 0.343062
FRAMES 1516; black []; unplanned white []; frozen spans >=12f []
POPS (unplanned frame-diff spikes > 3x local median): [518, 574, 782, 1165, 1342, 1441, 1515]
MOTION mean diff 3.69; frames with diff<0.3 (held): 71 (5%)

PER SHOT  (luma mean / std / p2 / p98 / saturation mean, medians over the shot)
  shot  0 f0-106: 0.296 / 0.261 / 0.039 / 0.974 / 0.401
  shot  1 f107-159: 0.336 / 0.247 / 0.069 / 0.971 / 0.423
  shot  2 f160-206: 0.334 / 0.245 / 0.080 / 0.972 / 0.414
  shot  3 f207-252: 0.355 / 0.270 / 0.093 / 0.979 / 0.389
  shot  4 f253-290: 0.382 / 0.281 / 0.101 / 0.985 / 0.371
  shot  5 f291-404: 0.459 / 0.227 / 0.118 / 0.971 / 0.332
  shot  6 f405-442: 0.453 / 0.220 / 0.117 / 0.970 / 0.327
  shot  7 f443-519: 0.580 / 0.219 / 0.092 / 0.770 / 0.240
  shot  8 f520-575: 0.391 / 0.240 / 0.114 / 0.975 / 0.428
  shot  9 f576-637: 0.377 / 0.239 / 0.111 / 0.980 / 0.431
  shot 10 f638-707: 0.375 / 0.240 / 0.114 / 0.980 / 0.430
  shot 11 f708-783: 0.397 / 0.248 / 0.115 / 0.975 / 0.411
  shot 12 f784-846: 0.397 / 0.247 / 0.115 / 0.980 / 0.411
  shot 13 f847-895: 0.386 / 0.266 / 0.115 / 0.985 / 0.390
  shot 14 f896-971: 0.303 / 0.161 / 0.006 / 0.706 / 0.482
  shot 15 f972-1051: 0.336 / 0.232 / 0.080 / 0.970 / 0.515
  shot 16 f1052-1115: 0.331 / 0.240 / 0.081 / 0.948 / 0.503
  shot 17 f1116-1141: 0.364 / 0.277 / 0.077 / 0.977 / 0.503
  shot 18 f1142-1173: 0.362 / 0.278 / 0.077 / 0.977 / 0.502
  shot 19 f1174-1285: 0.362 / 0.271 / 0.054 / 0.892 / 0.505
  shot 20 f1286-1315: 0.356 / 0.246 / 0.081 / 0.971 / 0.505
  shot 21 f1316-1343: 0.567 / 0.308 / 0.095 / 0.971 / 0.320
  shot 22 f1344-1450: 0.347 / 0.231 / 0.075 / 0.966 / 0.542
  shot 23 f1451-1515: 0.307 / 0.205 / 0.080 / 0.952 / 0.566

```

# Audio Quality Report

Status: PASS
Events: 7; distinct Wyzowl assets: 5

## Measurements

- duration_seconds: 50.53333333333333
- clipped_samples: 0
- sample_peak: 0.7594516277313232
- channel_rms: [0.14759035408496857, 0.14759035408496857]
- channel_difference_db: 0.0
- integrated_lufs: -14.0
- true_peak_dbtp: -2.0
- max_sync_error_frames: 0.0
- max_effect_to_voice_db_in_voiced_100ms: -26.615732192993164
- end_edge_peak: 0.0035555362701416016
- video: {'width': 1080, 'height': 1920, 'fps': '30/1', 'duration': 50.533333}

## Errors

- None.

## Warnings

- None.

## Scope

Against animation markers and sampled actual encoded frames; not automatic image contact detection.
Ducking plus a measured effect/voice proxy; not a human listening guarantee.

All selected library sources are CC0 with source URL, commit and SHA-256 retained in sfx-timeline.json. No paid API. Native approved voice files are read-only inputs.
