import os
import json

from datasets import Dataset, Audio

A_path = "C:/Users/zera/Desktop/A"
B_path = os.path.join(A_path, "B")
C_path = os.path.join(A_path, "C")

data = {
    "audio": [],
    "transcription": [],
    "start": [],
    "end": []
}

for json_file in os.listdir(C_path):
    if not json_file.endswith(".json"):
        continue

    json_path = os.path.join(C_path, json_file)
    with open(json_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    base_filename = meta["metadata"]["filename"]
    wav_path = os.path.join(B_path, f"{base_filename}.wav")

    for segment in meta["video"]["term"]:
        data["audio"].append(wav_path)
        data["transcription"].append(segment["transcription"])
        data["start"].append(segment["start"])
        data["end"].append(segment["end"])

# Hugging Face Dataset 생성
dataset = Dataset.from_dict(data).cast_column("audio", Audio())

# 예: train/validation 분할도 가능
dataset = dataset.train_test_split(test_size=0.1)

# 저장하려면
dataset["train"].to_csv("train.csv", index=False)
