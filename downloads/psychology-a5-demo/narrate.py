from pathlib import Path
import json,wave,hashlib,shutil
import numpy as np
import sherpa_onnx
b=Path(__file__).parent;m=Path('/workspace/local-models/piper-vi/vits-piper-vi_VN-vais1000-medium')
config=sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=str(m/'vi_VN-vais1000-medium.onnx'),tokens=str(m/'tokens.txt'),data_dir=str(m/'espeak-ng-data')),num_threads=4,provider='cpu',debug=False),max_num_sentences=2)
assert config.validate()
tts=sherpa_onnx.OfflineTts(config)
texts=["Vì sao ta dễ tin điều mình muốn tin? Anh chàng này nghĩ quầy táo quen luôn bán hàng ngon. Thấy quả đẹp, anh gật gù: đúng như mình nghĩ.","Gặp quả dập, anh lại bảo: chắc chỉ là ngoại lệ. Đó là thiên kiến xác nhận. Ta dễ chú ý bằng chứng ủng hộ niềm tin, rồi bỏ qua điều trái ngược.","Muốn nghĩ rõ hơn, hãy thử hỏi: bằng chứng nào có thể khiến mình đổi ý? Đừng chỉ tìm điều chứng minh mình đúng. Hãy kiểm tra cả điều mình không muốn tin."]
parts=[]
for i,text in enumerate(texts):
 gc=sherpa_onnx.GenerationConfig();gc.sid=0;gc.speed=1.0
 audio=tts.generate(text,gc);a=np.asarray(audio.samples,dtype=np.float32);sr=audio.sample_rate
 with wave.open(str(b/f'voice-scene-{i+1}.wav'),'wb') as f:f.setnchannels(1);f.setsampwidth(2);f.setframerate(sr);f.writeframes((np.clip(a,-1,1)*32767).astype('<i2').tobytes())
 parts.append({'scene':i+1,'text':text,'file':f'voice-scene-{i+1}.wav','duration':len(a)/sr,'sample_rate':sr})
 print(parts[-1],flush=True)
(b/'narration-parts.json').write_text(json.dumps(parts,ensure_ascii=False,indent=2));(b/'script-vi.txt').write_text('\n\n'.join(texts)+'\n')
shutil.copy2(m/'MODEL_CARD',b/'VOICE-MODEL-CARD.md')
(b/'voice-provenance.json').write_text(json.dumps({'engine':'sherpa-onnx OfflineTts / VITS Piper','model':'vi_VN-vais1000-medium','speaker':0,'rate':'native default, no tempo stretch','provider':'Local CPU; no voice API calls','source':'https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-vi_VN-vais1000-medium.tar.bz2','model_sha256':hashlib.sha256((m/'vi_VN-vais1000-medium.onnx').read_bytes()).hexdigest(),'model_card':'VOICE-MODEL-CARD.md','dataset_license_recorded_in_model_card':'CC BY 4.0; VAIS1000 corpus, https://ieee-dataport.org/documents/vais-1000-vietnamese-speech-synthesis-corpus'},ensure_ascii=False,indent=2))
