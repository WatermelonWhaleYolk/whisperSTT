from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import librosa

# 1. 모델과 프로세서 로드
model_dir = "./whisper-finetuned-final"
processor = WhisperProcessor.from_pretrained(model_dir)
model = WhisperForConditionalGeneration.from_pretrained(model_dir)

# ✅ 이거 꼭 해야 됨! 이거 없으면 오류 그대로 발생함
model.config.forced_decoder_ids = None
model.generation_config.forced_decoder_ids = None  # 이건 추가로 안전망

# 2. 오디오 파일 로드
audio_path = "test_korean_audio.wav"
audio, sr = librosa.load(audio_path, sr=16000)

# 3. 30초 단위로 자르기
chunk_size = 16000 * 30
chunks = [audio[i:i + chunk_size] for i in range(0, len(audio), chunk_size)]

results = []

# 4. 예측 반복
for chunk in chunks:
    inputs = processor(chunk, sampling_rate=16000, return_tensors="pt")
    input_features = inputs["input_features"]

    with torch.no_grad():
        predicted_ids = model.generate(input_features)

    text = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    results.append(text)

# 5. 결과 출력
print("\n📝 전체 Transcription:")
print(" ".join(results))
