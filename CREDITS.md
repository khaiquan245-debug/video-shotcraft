# Nguồn và công cụ

Lời kể do người dùng cung cấp, giữ nguyên thứ tự. Thiết kế nhân vật áo cam kế thừa phim “Điện thoại gọi về quá khứ” của chính dự án. Bối cảnh nhà, sân, đường dốc, thùng, cống, hố và bậc thoát, cục tẩy và hiệu ứng biến mất được vẽ/diễn hoạt trong production/film.mjs. Không dùng ảnh/slideshow hoặc lấy frame từ video mẫu.

Giọng: VieNeu-TTS v3 Turbo, Apache-2.0, ONNX CPU local, https://huggingface.co/pnnbao-ump/VieNeu-TTS-v3-Turbo . Preset thực tế Hải Đăng, alias Minh Quân trong adapter. Metadata WAV ghi rõ provider, nguồn và SHA. Model weights nằm ngoài Git/ZIP.

Nhạc nền 130 BPM và 79 sự kiện SFX/Foley được tự tổng hợp bằng oscillator/noise với NumPy. Các cue lăn nhẹ cũng được tính riêng; không phải 79 loại âm thanh. Không lấy soundtrack, giọng hoặc tiếng động của video mẫu. Audio theo hướng chà/xóa/lăn/sụt đất/chụp/rơi/leo/phản ứng, nhạc có ducking dưới lời dẫn.

Font Nunito: SIL Open Font License, kèm assets/OFL-Nunito.txt. Render bằng @napi-rs/canvas và FFmpeg, TTS local CPU. Không API trả phí hoặc cloud inference.
