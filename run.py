import whisper

model = whisper.load_model("small", device="cpu")
result = model.transcribe("data/bts_dynamite.mp3")
print(result["text"])