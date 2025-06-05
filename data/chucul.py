import pandas as pd
import os
import subprocess

df = pd.read_csv("cleaned_dataset.csv")
output_dir = "segments_ffmpeg"
os.makedirs(output_dir, exist_ok=True)

new_data = {
    "audio": [],
    "transcription": []
}

for idx, row in df.iterrows():
    audio_path = row["audio"].replace("\\", "/")
    transcription = row["transcription"]
    start = float(row["start"])
    duration = float(row["end"]) - start

    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    out_path = os.path.join(output_dir, f"{base_name}_{idx:05d}.wav")

    command = [
        "ffmpeg", "-y",
        "-ss", str(start),
        "-t", str(duration),
        "-i", audio_path,
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        out_path
    ]

    result = subprocess.run(command, capture_output=True)

    if result.returncode != 0:
        print(f"\n❌ 오류 발생 in {audio_path}")
        print("⚙️ ffmpeg 명령어:", ' '.join(command))
        print("📄 stderr 출력:\n", result.stderr)
    else:
        new_data["audio"].append(out_path)
        new_data["transcription"].append(transcription)

# 정상이면 저장
pd.DataFrame(new_data).to_csv("segments_dataset.csv", index=False)
