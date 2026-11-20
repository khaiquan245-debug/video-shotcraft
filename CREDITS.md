# Nguồn

Lời kể do người dùng cung cấp, giữ nguyên. Nhân vật chính kế thừa thiết kế của các Shorts trước; tranh nền chợ điện tử, căn phòng, quầy giày/vé số, biệt thự, người bán, điện thoại và các biến đổi được vẽ/diễn hoạt riêng bằng vector trong production/film.mjs. Không ghép khung hình hoặc soundtrack từ video mẫu.

Giọng: VieNeu-TTS v3 Turbo, Apache-2.0, ONNX CPU local; preset thực tế Hải Đăng, alias Minh Quân trong adapter. Nguồn model: https://huggingface.co/pnnbao-ump/VieNeu-TTS-v3-Turbo . Native WAV và checksum được bảo toàn; trọng số model không ở trong Git/ZIP.

Nhạc, Foley và nhạc chuông được tổng hợp bằng oscillator/noise trong production/audio.py. Nhạc chuông là chuỗi nốt tự viết, không lấy bản thu thương mại. Các tiếng phím dùng tần số chức năng DTMF. Câu cảnh báo cuối là cùng voice native qua EQ, không thêm lời nói mới.

Font Nunito theo SIL OFL, kèm assets/OFL-Nunito.txt. Không API trả phí, cloud inference hoặc subscription mới.
