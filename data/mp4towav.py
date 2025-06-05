import os
import subprocess

mp4_dir = "C:/Users/zera/Desktop/A/B"
wav_dir = mp4_dir

for filename in os.listdir(mp4_dir):
    if filename.endswith(".mp4"):
        mp4_path = os.path.join(mp4_dir, filename)
        wav_name = filename.replace(".mp4", ".wav")
        wav_path = os.path.join(wav_dir, wav_name)

        command = [
            "ffmpeg", "-y",
            "-i", mp4_path,
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            "-ac", "1",
            wav_path
        ]
        print(f"🎧 변환 중: {filename}")
        subprocess.run(command)
