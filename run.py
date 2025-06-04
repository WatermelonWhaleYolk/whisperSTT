import whisper

model = whisper.load_model("small", device="cuda")
result = model.transcribe("data/Myra.mp3")
print(result["text"])