from transformers import WhisperProcessor, WhisperForConditionalGeneration

model = WhisperForConditionalGeneration.from_pretrained("./whisper-finetuned/checkpoint-200")
processor = WhisperProcessor.from_pretrained("openai/whisper-small")  # ← 원본에서 불러와야 함

model.save_pretrained("./whisper-finetuned-final")
processor.save_pretrained("./whisper-finetuned-final")
