# PixiJS Environment Engine — kết quả thực tế

## Video và sửa tỷ lệ
- File hoàn chỉnh: `/workspace/video-shotcraft/output/pixijs_environment_demo.mp4`.
-15.000giây,1080×1920,H.264,60fps,900frame được tính riêng theo timeline; AAC48kHz stereo;15,700,826byte. Không watermark, không slideshow ảnh nền, không lời kể/nhạc mới.
- Theo phản hồi tỷ lệ nhân vật: giảm scale đồng nhất từ0.99 xuống0.30 tại mặt đất tham chiếu, so với chiều cao cửa hàng107đơn vị; ghế scale0.58. Camera tiến gần để thấy biểu cảm thay vì phóng to cơ thể so với cảnh. Giữ nguyên hình thể, chiều dài xương và artwork đã có; nhân vật nhỏ hơn ở lớp xa. Xem `qa/encoded-contact-sheet.png` và `preview/final-layout-10.5.png`.
- Cảnh: phố Việt Nam→theo chân nhân vật→gió/mây/những bông tuyết đầu→dừng/ngước nhìn→lùi ra toàn phố phủ tuyết.
- Bản render đầu đang chạy đã được dừng khi nhận phản hồi tỷ lệ; không coi bản đó là sản phẩm. Chỉ bản `picture-scaled-v2.mp4` được ghép âm thanh/xuất cuối.

##1. Phiên bản
PixiJS8.23.0, @pixi/3d0.1.0 (peer Pixi^8.23.0); Vite8.3.4, TypeScript5.9.3. Node24.22.1, npm11.9.0, FFmpeg7.1.5. Playwright/Chromium và native Rigby được tái sử dụng từ hệ thống đã cài.

##2–3. Skill chính thức và đường dẫn
Lệnh chính thức đã chạy: `npx --yes skills add https://github.com/pixijs/pixijs-skills --agent codex --skill pixijs pixijs-3d --yes --copy`.
- `.agents/skills/pixijs/SKILL.md`
- `.agents/skills/pixijs-3d/SKILL.md`
Nguồn MIT, commit93784384269b1d8677fb2ae166c81d750cba4281. Đã đọc README/LICENSE và các tham chiếu API liên quan. Tổng83file gồm81file tham chiếu, so sánh byte/hash khớp upstream. Không sửa skill chính thức. Bằng chứng: `qa/official-skills-integrity.json`; chạy lại `node integrations/pixijs-environment/integrity.mjs`.

##4. Dependency và cài lại
Package/lock/node_modules được tách tại `integrations/pixijs-environment/`, không sửa package-lock của ứng dụng. `node integrations/pixijs-environment/setup.mjs` cài dependency đã pin; `--verify` kiểm tra hiện trạng mà không cài lại. Source tool và node_modules được ignore. Không có model weights mới, không có paid API/cloud inference. Mọi tài nguyên demo chạy local/offline sau khi cài.

##5. Module thực thi
- model: seed, cấu hình, registry, weather/light/camera state, tỷ lệ, phân tích kịch bản bằng luật rõ ràng.
- art/templates: façade nhiều chi tiết, cửa sổ/ban công/mái/biển hiệu/cây/ghế/xe/đèn và5môi trường.
- engine:7lớp ngữ nghĩa, parallax, cùng mặt phẳng Y-sort cho nhân vật/đồ vật, che khuất, bóng chiếu, window mask, độ sâu khí quyển, blur lớp xa tùy chọn.
- weather: ParticleContainerv8/addParticle và shaderGLSL; lighting ảnh hưởng chung nhân vật/cảnh.
- motions: cỏ/water mesh deformation, khói/lửa/thác hạt, bánh xe/piston, vật rơi/nảy analytic.
- three: View3D thật, depth buffer, terrain289vertex,150box mesh,18nhóm cây, perspective camera, directional shadow, point/hemisphere light, fog.
- browser/render: Chromium→900frame JPEG theo i/60→FFmpeg. `render-timeline.mjs` hỗ trợ manifest nhiều cảnh đã được tác giả xác định, audio/caption có sẵn.
- sound: ambience/foley tổng hợp local; adapter sound director hiện hữu chọn2cue WyzowlCC0 có nguồn/hash/marker.

##6. Số template thực tế
**5template2D/2.5D:** đường phố Việt Nam, rừng, sa mạc, phòng ngủ, bãi biển. Thêm **1cảnh thử nghiệm low-poly3D độc lập**; không tính là51template đã hoàn thành. Tùy biến màu/mật độ/bố cục phong phú nhất ở phố/rừng; các template còn lại chưa có đầy đủ mọi biến thể.

##7. Hiệu ứng/camera
13preset thời tiết và12preset ánh sáng đã chạy setTime/app.render trong trình duyệt, không báo lỗi. Có cây/lá/cỏ/mây/chim/xe/đèn/cửa/rèm/thuyền, sóng mesh, khói/lửa/thác hạt, bụi, tuyết tích tụ, máy móc và vật rơi. Motion library bổ sung đã render riêng ở `qa/optional-effects.png`; không khẳng định toàn bộ hiệu ứng xuất hiện trong15s demo.
20camera preset đã đăng ký/kiểm tra trạng thái. Góc high/bird/worm yêu cầu3D thật; có ảnh kiểm tra góc low và bird ở `qa/3d-*.png`. Ở2.5D, low/POV/OTS là crop/bố cục gợi ý; muốn đổi hướng nhìn thật phải bổ sung artwork/3D. Demo chính không quay từ trên cao.

##8. Tích hợp Rigby2D
Native runtime Pixi của Rigby0.6.1,23xương,4IK chain,21vùng atlas và weighted mesh. Không chèn toàn nhân vật bằng một PNG chuyển động. Clip đi bộ/dừng/ngước nhìn15s,901mẫu;16bước có marker. Tay không vượt tầm; quần áo và tóc phản ứng với gió.901mẫu runtime: sai số độ dài xương tối đa3.56e-14; sai số đầu chi1.25e-13; dịch chuyển khớp/frame lớn nhất4.014đơn vị; khuỷu tay hướng ngoài ở đoạn giơ tay. Kiểm tra đầu gối ngồi/nhặt và cầm/nâng hướng ngoài của adapter cũ vẫn đạt.
QA sắp xếp ghế trước nhân vật ở cùng mặt phẳng và ảnh che khuất được lưu `qa/occlusion-calibration.png`. Demo không có động tác cầm đồ, nên không tuyên bố đã kiểm chứng cầm mọi vật thể tự động.

##9. Skill riêng
`/workspace/video-shotcraft/.agents/skills/pixijs-environment-director/SKILL.md`
Có references/scripts/examples/templates/assets/tests; AGENTS.md được nối thêm hướng dẫn sử dụng và kiểm tra tỷ lệ. Những block cũ giữ nguyên.

##10. Kiểm thử thực chạy
-10/10kiểm tra model mới: seed, template validation,13weather/12light, tuyết,20camera, tính liên tục, parallax, tỷ lệ, kịch bản quay lại/địa điểm chưa hỗ trợ, vật rơi.
-13/13kiểm tra tích hợp Rigby,23/23kiểm tra ứng dụng cũ.
-9trường hợp browser:5template hai thời điểm +4style bổ sung; deterministic replay khớp ảnh, ảnh thay đổi theo thời gian, không pageerror. City cartoon là style thứ5.
-901tư thế native, density/layout, thứ tự ghế/nhân vật;3D low/bird render thành file.
-`tsc --noEmit` đạt trên file API contract của package đã cài (không tuyên bố toàn bộ JS đã strict typecheck).
-Vite build đạt; có cảnh báo bundle lớn, không có build error.
-Exporter nhiều cảnh:0.4s/24frame forest→beach; nhánh audio/caption thử bằng test tone tự tạo và SRT tiếng Việt, H.264/AAC/mov_text; đây là kiểm tra mux đồng bộ, không phải giọng đọc mẫu.
-FFprobe cuối:900frame/60fps/1080×1920/15s; FFmpeg giải mã toàn bộ không lỗi. Đã xem contact sheet trích từ MP4.
-Âm thanh cuối: -13.7LUFS, -1.6dBTP,0clipped samples,2cue có metadata; QC đạt không warning. Báo cáo: `final/audio-quality-report.md`. Foley bước chân là tổng hợp nguyên gốc; cue vải/shimmer làCC0. Không thay/ghi đè narration đã duyệt.
-Xem `qa/playback.json` cho kết quả phát kỹ thuật trong Chromium; đây không phải nghe thẩm định bằng người.

##11. Đầu ra
MP4 chính ở đường dẫn đầu báo cáo. Source có thể xem/chạy bằng `npm run dev --prefix integrations/pixijs-environment`. Vì Vite từ chối đường dẫn MP4 ngoài public vớiHTTP403, preview MP4 dùng local HTTP server riêng cổng8865; không phải lỗi decode video. Đường tải GitHub được lưu riêng sau khi upload vào nhánh downloads; không push/merge main.

##12. Giới hạn
Chưa xây toàn bộ51môi trường; parser chỉ là luật từ khóa, có requiresAuthoring/unresolved, không tự đạo diễn mọi kịch bản. Giữ seed/weather tại địa điểm đã biết; chưa có semantic understanding hoặc tự tạo mọi prop/pose.2D light/shadow/DOF là mô phỏng nghệ thuật, không physical GI; tsunami/thác/lửa là hiệu ứng cách điệu, không fluid simulation. Rigby vẫn là2D trong cảnh2.5D; chưa chuyển nhân vật thành rig3D. POV/OTS đổi hướng thật cần asset bổ sung. Caption adapter dùng mốc có sẵn, không có forced alignment tiếng Việt mới. No new narration/music. Chưa benchmark trênGTX1060 thật; bản1080p được render bằng CPU SwiftShader khoảng221giây cho15giây phim.

## Lỗi gặp và xử lý
- Route preview Vite ngoài public:HTTP403 localhost8864; dùng HTTPserver riêng, MP4 thật đã probe/decode thành công.
- Smoke test exporter lần đầu giữ closure trỏ canvas đã destroy; sửa sang canvas của engine hiện hành, chạy lại thành công ở `timeline-smoke-v2.mp4`.
- Cue shimmer ban đầu bị lọc nhầm category; bỏ ràng buộc sai, sound director cuối chọn đủ2cue, không missing.
- Không gặp lỗi tải npm/GitHub trong lần cài này. Không tải lại browser/model hay dùng dịch vụ trả phí.

## Bảo toàn
SHA256 phim Rigby trước đây vẫn ccd99e56089a92a8f4d094b1e7c82a522a2f6923482c4d9c22c613d42a0d0b27. SHA256 MP4 mới:5b251457190b7530b0819c1a2b7caff15af2e3b1fde09b2e878bac4266c2b3e8. Output mới nằm thư mục riêng; các project/artwork/narration cũ không bị ghi đè.
