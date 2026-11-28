# Lời nói dối của mẹ — V5

- Giữ kịch bản gồm 24 đoạn thoại, nhận diện và đường tiếng đã duyệt. Bản V5 có thư mục render độc lập và dùng lại lịch thoại, hiệu ứng âm thanh, phụ đề gốc.
- Nhân vật hoạt hình 2D nhiều bộ phận đứng trong không gian 3D. V5 tách dáng đứng, đi, nói và ngồi, có hàm bước chạy cho cảnh cần, mỗi vai dùng pha riêng. Đoạn đứng yên giảm khuỵu gối, các cuộc trò chuyện có hướng thân và hướng mắt riêng theo vai. Tác vụ kiểm tra toán học xác nhận chiều dài hai đoạn tay ở các mục tiêu thử và điểm chân trụ theo hình chiếu cho một đoạn đi thẳng.
- Đã cập nhật bảy địa điểm. Cà phê có biển menu, bàn phụ, khách và phục vụ; phố có thêm biển cửa hàng, vỉa hè và xe máy; mặt tiền có garage, sân và phần hồ bơi; tiệc có bóng bay, đồ ăn, khách nâng cốc; nhà mẹ có bổ sung ngói, lối sân và đồ dùng. Căn bếp dùng lại bộ V4 với normal map, ánh sáng từ đèn bàn ăn và tủ lạnh có bản lề.
- Camera dùng đường cong 3D và kiểm tra liên tục ở mọi khung. Có tám lần cắt được khai báo, gồm cắt đổi địa điểm và chuyển vào/ra POV tủ lạnh. Cà phê, cú hé lộ biệt thự và camera qua khách dự tiệc được bố cục lại.
- Điểm chân trụ được tính trong hình chiếu của nhân vật 2D ở các đường đi đã gắn đường chạy. Vẫn chưa có bộ kiểm tra va chạm toàn thân hoặc IK 3D tổng quát cho mọi cặp nhân vật và đạo cụ. Bản mẫu có dựng tương tác tủ theo điểm bản lề. Các động tác có thể còn đơn giản so với hoạt hình nhân vật 3D đầy đủ.
- Runtime dùng Three.js, module Cinematic 3D World & Camera Director và bếp V4. Tài sản Kenney/KayKit CC0 và quỹ đạo camera có từ pipeline V3 được tái dùng. Đường tiếng Wyzowl hiện có được chép nguyên từ bản gốc.

## Kiểm tra bản MP4

```text
SPECS 1080x1920 30/1 fps, 1516 frames, 50.533 s; audio: aac 48000 Hz 2ch
LOUDNESS I:         -14.0 LUFS | LRA:         1.5 LU | Peak:       -2.0 dBFS
SILENCES silence_start: 41.072292; silence_end: 41.529688 | silence_duration: 0.457396; silence_start: 48.014937; silence_end: 48.358 | silence_duration: 0.343062
FRAMES 1516; black []; unplanned white []; frozen spans >=12f []
POPS (unplanned frame-diff spikes > 3x local median): [518, 782, 1165, 1342, 1441, 1515]
MOTION mean diff 3.61; frames with diff<0.3 (held): 27 (2%)

PER SHOT  (luma mean / std / p2 / p98 / saturation mean, medians over the shot)
  shot  0 f0-106: 0.294 / 0.257 / 0.040 / 0.965 / 0.368
  shot  1 f107-159: 0.353 / 0.255 / 0.085 / 0.969 / 0.389
  shot  2 f160-206: 0.346 / 0.251 / 0.085 / 0.969 / 0.386
  shot  3 f207-252: 0.348 / 0.265 / 0.093 / 0.969 / 0.367
  shot  4 f253-290: 0.374 / 0.276 / 0.103 / 0.976 / 0.352
  shot  5 f291-404: 0.445 / 0.225 / 0.131 / 0.963 / 0.325
  shot  6 f405-442: 0.438 / 0.218 / 0.129 / 0.958 / 0.322
  shot  7 f443-519: 0.562 / 0.210 / 0.098 / 0.766 / 0.242
  shot  8 f520-575: 0.376 / 0.235 / 0.122 / 0.969 / 0.417
  shot  9 f576-637: 0.362 / 0.232 / 0.114 / 0.972 / 0.419
  shot 10 f638-707: 0.359 / 0.233 / 0.119 / 0.972 / 0.419
  shot 11 f708-783: 0.377 / 0.238 / 0.127 / 0.972 / 0.402
  shot 12 f784-846: 0.374 / 0.236 / 0.123 / 0.972 / 0.404
  shot 13 f847-895: 0.365 / 0.249 / 0.122 / 0.976 / 0.389
  shot 14 f896-971: 0.293 / 0.164 / 0.017 / 0.707 / 0.471
  shot 15 f972-1051: 0.342 / 0.225 / 0.095 / 0.960 / 0.476
  shot 16 f1052-1115: 0.337 / 0.233 / 0.095 / 0.937 / 0.467
  shot 17 f1116-1141: 0.369 / 0.269 / 0.094 / 0.969 / 0.465
  shot 18 f1142-1173: 0.367 / 0.270 / 0.095 / 0.970 / 0.463
  shot 19 f1174-1285: 0.367 / 0.269 / 0.095 / 0.969 / 0.464
  shot 20 f1286-1315: 0.362 / 0.240 / 0.096 / 0.964 / 0.468
  shot 21 f1316-1343: 0.569 / 0.302 / 0.101 / 0.964 / 0.300
  shot 22 f1344-1450: 0.353 / 0.224 / 0.090 / 0.956 / 0.502
  shot 23 f1451-1515: 0.315 / 0.200 / 0.095 / 0.945 / 0.521

```
