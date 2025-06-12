from transformers import WhisperForConditionalGeneration, WhisperProcessor

model = WhisperForConditionalGeneration.from_pretrained(
    "../whisper-finetunedv2/checkpoint-1000",
    local_files_only=True
)
# 생성된 체크포인트 명
processor = WhisperProcessor.from_pretrained(
    "../whisper-finetunedv2/checkpoint-1000",
    local_files_only=True
)

model.save_pretrained("../zeraV03") # 저장할 폴더 이름
processor.save_pretrained("../zeraV03")
