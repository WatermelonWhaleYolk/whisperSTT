import whisper

model = whisper.load_model("tiny", device="cpu")
result = model.transcribe("tests/jfk.flac")
print(result["text"])