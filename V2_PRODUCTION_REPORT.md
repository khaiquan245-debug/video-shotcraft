# Sao chép kỹ năng trong 24 giờ — V2

## Tệp thực tế

`/workspace/outputs/skill-copy-24h-cinematic-V2-20261126/final/Sao_Chep_Ky_Nang_24h_Cinematic_V2_1080p30.mp4`

**418.100 giây (6 phút58giây), 1920×1080 gốc, 30 fps, 12,543 khung hình, H.264/AAC48kHz stereo.** Không upscale bản720p. Dung lượng: 117,294,815 byte (111.86 MiB). SHA-256: `32abc0bbf1cc52cf6038896b6d35d206c3a709da058334c0dfe8fb7ec1c7d227`.

Bản demo trước khi render toàn bộ: 23,233 giây /697 khung hình, cùng1920×1080/30fps, đã kiểm tra MP4 và phát/tua trong Chromium. Demo được sửa cận phản ứng và biểu tượng piano hết hạn trước khi chốt cách dựng. Những chỉnh sửa sau demo chỉ hoàn thiện các cảnh không nằm trong demo: bàn tay POV, giao dịch và biển trang trí bị camera cắt. Kiểm tra MP4 phát hiện clip ngồi bị dùng nhầm cho người quay/người nhận đồ; đã render lại các đoạn20/30/35 bằng clip đứng và bỏ chiếc thìa lúc trao món ăn; bổ sung ghế/bàn phím đúng vị trí và hướng ngồi cho đoạn70/71/72, ghế cho clip nhỏ trong điện thoại tại đoạn75; đặt kiện hàng xuống sàn và áp dụng bố trí nhân viên đúng cho các đoạn80–83. Bản picture làm việc được giữ; lắp11đoạn sửa vào bản cuối bằng trim/concat đúng khung hình, vẫn1920×1080/30fps, giữ nguyên audio/timing. Audit nằm trong actor-role-repair.json.

## Biên tập và lời kể

Giữ thông điệp, các quy luật, hành trình kiếm tiền–giới hạn thể chất–xây doanh nghiệp–học thật–giải cứu và kết luận của kịch bản. Bỏ10 đoạn mở đầu giới thiệu/đặt câu hỏi rồi kể lại; chuyển ba đoạn giới hạn vào sau lần thử đàn thất bại. Còn **126 đoạn lời kể, 1708 tiếng theo cách đếm dấu cách**. Có `207` cụm phụ đề. Chi tiết trong`source/editorial-changes.json` và`manifests/film.json`.

Cú bắt tay truyền năng lượng xuất hiện tại0,73giây. Không có intro logo dài. Lời kể là các đoạn VieNeu-TTS v3 Turbo đã tạo cục bộ (ONNXfp32 Apache-2.0, SDK3.8.4), Minh Quân là alias được adapter ánh xạ sang preset Hải Đăng. Không tạo lại giọng. Biên tập trên WAV riêng và dùng`atempo=1.06` giữ cao độ, theo yêu cầu tăng nhịp6%. Tệp gốc/V1 vẫn nguyên hash. Không gọi API hoặc suy luận trả phí.

## Thay đổi hình ảnh và đạo diễn

| Yêu cầu | Thực hiện trong V2 |
|---|---|
| Mở tình huống ngay | Chạm tay, luồng năng lượng từ lòng bàn tay đến đầu, skill unlocked và24h xuất hiện trong3giây đầu. |
| Nhân vật lớn, giảm khoảng trống | Chủ yếu trung/cận, cận phản ứng và cận tay; toàn/reveal dùng cho không gian làm việc và cứu hộ. |
| Nhiều loại shot | CU/ECU, góc qua vai với hình lưng vẽ theo xương, insert POV điện thoại/bản nhạc, tracking, dolly ngang, parallax, reveal. Đây là các góc vẽ2D riêng và bố cục phân lớp, không phải tuyên bố camera3D vật lý. |
| Hành động theo lời kể | Bắt tay, ngồi xuống/đặt tay/chơi đàn, cờ-lê/động cơ, khuấy nồi, trao món ăn và tiền, bàn phím/lỗi, nâng tạ thất bại, ghi chép, từ chối, điều khiển robot và rời khu nguy hiểm. |
| Bối cảnh | 21 không gian theo tình huống: cafe, gara, bếp, phòng lập trình ban đêm, studio, quầy bán ngoài trời, boxing, tạ, sân chạy, nhà, kiến trúc, tài chính, họp, học, cố vấn, doanh nghiệp, sân khấu mạng xã hội, nghiên cứu, lab, đường phố và đồ hoạ bộ nhớ. Không ghép bàn/tủ nội thất vào đường phố. |
| Chuyển động độc lập | Nhân vật dùng bộ xương43xương,20xương ngón tay. Camera, nền xa, nền giữa, tiền cảnh, bụi, hơi nước và các đạo cụ động có sampler riêng. Không phải pan/zoom một ảnh toàn cảnh. |
| Tương tác và tư thế | IK giữ chiều dài xương, chân trụ, hai gối hướng trước khi ngồi/cúi, khuỷu nâng tạ hướng ngoài. Bàn tay POV có hai đoạn cánh tay cố định và ngón nối vào lòng bàn tay. Chỉnh điểm thìa chạm mặt nồi, vị trí người nhận đồ, bàn nhân viên, mũ và tay bị thương. |
| Biểu cảm | Miệng, mắt, mày, hướng nhìn, đầu và vai thể hiện ngạc nhiên, vui/tự tin, lo lắng, thất vọng, hoảng hốt và nhẹ nhõm. Không có phoneme lip-sync chính xác cho lời dẫn. |
| Hệ thống kỹ năng | Truyền năng lượng, mở khoá, một slot thay thế, countdown, tan kỹ năng và sản phẩm/ghi chép còn lại. |
| Kiếm tiền/doanh nghiệp/danh tiếng | Trao món/tiền, quầy hàng, nhân viên cùng làm việc, thùng hàng, điện thoại phát nhân vật đang biểu diễn và số lượt xem, lời mời, hợp đồng và từ chối. |
| Cao trào | Lab có ánh cảnh báo, góc cận tay băng bó và console, cận robot/nạn nhân, robot mở cổng rồi hỗ trợ người đi ra bằng chuyển động chân thực sự trong phong cách hoạt hình. |
| Kết phim | Montage trở lại đàn, bếp, code, thể thao, cố vấn, học tập, kỹ năng phai và ứng dụng tự sửa được; kết bằng lời mời lựa chọn. Không giữ nhân vật cạnh bảng chữ. |
| Phong cách kênh | Giữ nhận diện nhân vật3/4, tóc đen, áo sáng/navy và đường nét hoạt hình; dùng nhận diện chữ“THÍCH HỌC HỎI”. |

## Âm thanh

Chọn **44 cue** bằng skill`wyzowl-sfx-director`, từ Wyzowl SFX Kit CC0-1.0, theo marker hành động30fps và metadata`use_for/avoid_for/tags/sync.at`. Đã giới hạn loại âm để tránh tiếng swipe/riser bị chọn cho giấy hoặc bàn phím. **0 whoosh** trong danh sách cuối; không gắn âm vào mọi cut. Nhạc/foley tổng hợp cục bộ có nhịp học tập, căng thẳng cứu hộ và đoạn kết ấm hơn; piano, bước chân, vật liệu và vỗ tay có marker riêng. Nguồn/hash/giấy phép lưu trong`sfx-timeline.json` và`mix-manifest.json`.

AAC của MP4 đo được **-14.0 LUFS**, true peak **-1.7dBTP**; master có **0 mẫu clipping**. AudioQC đạt, không lỗi/cảnh báo. Độ rõ giọng được đánh giá bằng ducking và proxy mức che lấp, chưa thay thế nghe thẩm mỹ toàn bộ bằng người.

## Kiểm tra thực tế và giới hạn

- Bộ test Rigby13/13 và môi trường10/10 đạt; build riêng cho entry V2 thành công (cảnh báo bundle JS lớn500kB, không ảnh hưởng MP4).
- FFprobe đếm đủ12,543khung hình,1920×1080/30fps; công cụ âm thanh giải mã video/audio đầy đủ, kiểm tra chính MP4 sau mux.
- Kiểm tra126đoạn trong trình duyệt (504mẫu): không lỗi runtime, request, reach IK, phụ đề vượt vùng đặt hoặc danh mục nội thất ở cảnh ngoài trời. Chỉnh sửa cuối được kiểm tra thêm22mốc tay/đàn/bếp/giao dịch/POV/cứu hộ/kết.
- 5,973mẫu động tác: sai số chiều dài xương tối đa5e-14, sai số tip IK1.7e-13, trượt chân trụ1.7e-13, không phải chiếu lại mục tiêu tay vượt tầm. Có kiểm tra riêng101mẫu cánh tay POV. Các số đo không chứng minh mọi hình vẽ đều tự nhiên.
- Lấy16khung hình từ MP4 thật cho contact sheet. Phát/tua đầu phim, cứu hộ và kết trong Chromium; đây là kiểm tra kỹ thuật tắt tiếng, không phải nghe/xem thời gian thực toàn bộ bằng người.
- Phụ đề dựa trên thời lượng từng đoạn WAV đã đo, chia nhóm chữ theo tỷ lệ. Chưa forced-align từng từ/âm vị. Chữ và caption có lề trong khung; cận cảnh có thể chủ đích cắt thân người/đạo cụ, không phải cam kết mọi vật thể đều nằm trọn khung.
- V2 là hoạt hình vector phân lớp2.5D. Ánh sáng/bóng là đồ hoạ và gradient, không GI/PBR3D, motion capture hay mô phỏng cơ khí/âm nhạc chuyên môn. Kiểm tra kỹ thuật không tự chứng nhận chất lượng“cinematic thực sự”; mức đẹp/tự nhiên vẫn là đánh giá thẩm mỹ.
- Giữ V1 MP4 hash`1a88e598f1376fb923326424b3e56f640936b57edc095b542f7a5b7655adaa1e` và narration gốc`353fb665d5f809907e612538e99bac75e3e650f4608edd2f8c89902edd2b5172`. Không sửa skill hay dự án Video Shotcraft cũ. Trọng số TTS ngoài Git.

Mỗi phần24giây có checkpoint và chữ ký nguồn. Tái dùng lời kể, rig, âm thanh và các phần render hợp lệ; không dùng slideshow, không mua API/subscription. API GitHub Releases tại api.github.com trả lỗi Forbidden vì host chưa nằm trong allowlist hiện hành. Git push và raw download đã hoạt động với demo. Nếu master vượt100MiB, giữ nguyên master trong workspace và xuất bản tải H.264 riêng dưới100MiB, vẫn1920×1080/30fps và giữ nguyên các packet AAC. Chi tiết kích thước/hash/so sánh ảnh của bản tải nằm trong download-verification.json; không giả vờ đã upload master qua Releases.


Kiểm tra binding sau remux: SHA-256 của các packet video trong MP4 master trùng chính xác với picture đã sửa11đoạn (`final-mux-binding.json`). Bản master cuối có hash32abc0bbf1cc52cf6038896b6d35d206c3a709da058334c0dfe8fb7ec1c7d227; bản hình trung gian trước khi sửa được lưu riêng, không dùng để giao.
