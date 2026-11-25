# Rigby2D — báo cáo cài đặt và kiểm thử thực tế

## Kết quả

Đã cài nguồn Rigby2D **v0.6.1**, commit **8fdea6dd7689355bfea54a11371f275fa1391dd3**, tại `tools/rigby2d`. Node24.22.1, Python3.12.14 và FFmpeg7.1.5 đã có sẵn. Không dùng API trả phí/GPU thuê. Bản nguồn dual-licenseMIT/Apache-2.0. Không cài desktopTauri/Rust vì runtimeJavaScript và CLI đáp ứng bài kiểm thử.

Đã chạy npm install trong checkout riêng:197package; lần đầu lỗi tải thư việnGPU được khắc phục bằng cờ chính thứcONNXRUNTIME_NODE_INSTALL=skip. CPUONNX đi kèm npm đã nạp được. Dependency trực tiếp gồm: @anthropic-ai/mcpb@2.1.2, @emnapi/runtime@1.11.3, @huggingface/transformers@4.3.1, @img/sharp-wasm32@0.35.5, @lucide/lab@0.13.0, @tauri-apps/api@2.12.3, @tauri-apps/cli@2.12.2, @tauri-apps/plugin-dialog@2.8.2, @tauri-apps/plugin-fs@2.7.0, @tauri-apps/plugin-http@2.8.3, @tauri-apps/plugin-opener@2.7.2, @tauri-apps/plugin-process@2.4.0, @tauri-apps/plugin-updater@2.14.1, ag-psd@31.0.3, highlight.js@11.12.0, lucide@1.73.0, marked@18.1.1, pixi.js@8.22.0, playwright@1.64.1, pyodide@314.0.7, tslib@2.8.1, tsup@8.5.1, tsx@4.23.15, typescript@5.9.3, vite@8.3.4. Adapter dùng @napi-rs/canvas0.1.100 trong package/lock riêng. Các lockfile ứng dụng cũ không bị sửa.

## Tệp/module

- `integrations/rigby2d/`: character/artwork tách lớp, motions50, adapter native, planner local, generic environment, renderCPU, pipeline, CLI, setup, MCP probe/launcher, Remotion bridge, tests và ví dụ.
- `.agents/skills/rigby2d-character-animation/SKILL.md` cùng scripts/references/examples; AGENTS.md chỉ được **thêm** phần hướng dẫn tích hợp mới, giữ nguyên nội dung cũ.
- `.codex/config.toml`: cấu hình MCP giới hạn root trong repository. `tools/.gitignore` giữ checkout ngoài index; setup tái tạo đúng commit.
- `output/rigby2d/characters/hero-library-50-v3.rigby`: **50clip có timeline thật**. `hero-demo-v6.rigby`: rig demo đã sửa khớp. Các bản thử bị loại được giữ ở preview/characters và không phải bản giao.
- `output/rigby2d_animation_demo.mp4`: bản giao **10giây,1080×1920,60fps,600frame**, H.264/AAC. SHA256:ccd99e56089a92a8f4d094b1e7c82a522a2f6923482c4d9c22c613d42a0d0b27.

## Chức năng đã chạy

Rig23bones,20slots/21images tách lớp,4chuỗiIK hai xương, FK độc lập, native AnimationState blending, keyframe/nội suy mượt, retarget1.3x, mesh áo9đỉnh có trọng số và deform keys, tóc/áo chuyển động phụ, lấy đà/followthrough/squash vải, chuyển trọng tâm kinematic, khóa chân theo contact thế giới, gaze/chớp mắt/lông mày/khẩu hình và gesture. Chỉ phần thân có mesh trọng số; không tuyên bố tự dựng toàn thân từ mộtPNG. Hiệu ứng hair/cloth và cân bằng là mô hình kinematic, không phải mô phỏng động lực học người hoàn chỉnh.

Cả50action trong catalogue đã được bake và lấy mẫu bằng runtime native. Mỗi controller có speed,direction,intensity,duration,loop. Retarget/bone mapping được kiểm thử cho rig tương thích lớn hơn1.3x. Tư thế gốc khác/nhân vật phi chuẩn vẫn cần mapping và kiểm tra contact; loop root-motion phải tích lũy offset, không replay teleport.

**Sửa theo phản hồi mới:** cả hai gối gập theo cùng phía trước (không xòe ngang); khuỷu tay mở ra ngoài khi cầm/nâng, kể cả tay giữ bóng khi nhân vật ngạc nhiên. Test riêng kiểm tra các điều kiện này.

Planner offline nhận câuVI/EN, tên actor tường minh, cue hành động/cảm xúc, nối hành động và nhận timing câu đã đo. `produce` đã xuất MP4 thật từ fixture; background/camera/giọng/SFX cũ dùng như các layer đầu vào. Parser là luật xác định, **không hiểu mọi kịch bản tùy ý**. Cần tác giả/agent chỉnh anchor, tương tác, view và cue chưa nhận diện trước phim thật. Timing ví dụ5giây là fixturekỹ thuật, không giả nhận là lời đọc đã đo.

Lip-sync đã kiểm thử với timing word/viseme chuẩn qua native engine, và đo RMS đoạnWAV1.5giây (90frame,9cue) từ bản ghi cũ bằng đọc trích đoạn, không sửa bản gốc. RMS chỉ điều khiển mở/đóng miệng; **chưa có căn chỉnh âm vị tiếng Việt tự động chính xác**.

## Kiểm thử

- Upstream:402test,400pass,0fail,2skip (giữ đúng trạng thái upstream, không gọi là402pass).
- Ứng dụng cũ:23/23helpertestpass; thêm vitest.config.ts để tách testNode của tool/adapter và skillthirdparty khỏi suiteVitest ứng dụng.
- Adapter:13/13testpass, gồm50motion, IK/FK/blend/deform/retarget, lưu không ghi đè, parser, hai khóa gối/chỏ và tay cầm bóng xuyên suốt phản ứng.
- Native validate demo và50clip:valid,không lỗi/cảnh báo,JSONroundtrip vàbinaryexportok.
- CLI gốc đã render2PNG thật bằng Chromium/SwiftShaderCPU. Tải browserPlaywright bị chặn; không giả nhận đã tải thành công.
- Remotion: composition riêng đã bundle/render1080×1920still thực với layeralpha, không sửa composition workbench.
- MCP stdio:handshake/list60tools/inspect thành công; đường dẫn ngoài root bị từ chối. Codex với override cấu hình tường minh nhận serverenabled. LệnhCLI mặc định chưa tự nạp project MCP; **không có hot-registration vào tools của cuộc trò chuyện này**. Dùng CLI hiện tại hoặc launcher `node integrations/rigby2d/codex-launch.mjs ...` cho phiên được cấu hình; không ghi configglobal bị bảo vệ.
- Demo600frame: maxboneerror=2.842170943040401e-14; maxIKtiperror=9.953940410498703e-14; stancefootdrift=1.7763568394002505e-15; meshfoldovers=0; knee-forward-min=37.860430781593834; elbow-outward-min=14.092695927736386 (đơn vịrig). Các số đo không thay cho đánh giá diễn xuất bằng hình.
- Âm thanh:-14.5LUFS,-1.9dBTP,0clippedsample; nhạc tổng hợp gốc, bước chân tổng hợp theo contact và3WyzowlCC0cue. Demo không lời dẫn; không revoice file đã duyệt.
- Phát Chromium cómute là kiểm thử kỹ thuật, không phải chứng nhận đã nghe thẩm âm. Xem `qa/playback.json` để biết kết quả thực tế.

## Lỗi mạng và giới hạn còn lại

- rigby2d.com: HTTP403 on official web docs; official checked-out Markdown used instead
- api.nuget.org: onnxruntime-node postinstall getaddrinfoEAI_AGAIN on additionalGPU binaries; official ONNXRUNTIME_NODE_INSTALL=skip resolved installation; bundled CPU backend loaded
- cdn.playwright.dev: HTTP403 Domainforbidden downloading Chrome forTesting156.0.8078.4; systemChromium156.0.8078.79 is controlled through installedPlaywright1.64.1 instead

Chưa có tự động semantic-scene generation cho mọi thể loại, reconstruct/rig mộtPNG phẳng, căn chỉnh âm vịVI chuẩn hay full-bodyphysicalCOMsolver.50stockaction là prototypekinematic có kiểm thử, cần đạo diễn/contactreview cho đạo cụ và góc nhìn cụ thể. PhiênMCP hiện tại dùng fallbackCLI hợp lệ. Không tự ý xuất bản môi trường, đổi main, xóa các phim hoặc sửa giọng cũ.
