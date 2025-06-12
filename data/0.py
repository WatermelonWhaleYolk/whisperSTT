# 4_mp4_to_wav.py
import os
import subprocess

mp4_dir = "./A/B"
wav_dir = mp4_dir

failed_files = []  # 변환 실패 파일 리스트

for filename in os.listdir(mp4_dir):
    if filename.endswith(".mp4"):
        mp4_path = os.path.join(mp4_dir, filename)
        wav_name = filename.replace(".mp4", ".wav")
        wav_path = os.path.join(wav_dir, wav_name)

        # 이미 변환된 파일 건너뜀
        if os.path.exists(wav_path):
            print(f"✅ 이미 존재: {wav_name} → 건너뜀")
            continue

        command = [
            "ffmpeg", "-y",
            "-i", mp4_path,
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            "-ac", "1",
            wav_path
        ]

        print(f"🔁 변환 중: {filename} → {wav_name}")
        result = subprocess.run(command, capture_output=True)

        if result.returncode != 0:
            print(f"❌ 변환 실패: {filename}")
            failed_files.append(filename)

# 모든 변환 시도 후, 실패 파일 출력
if failed_files:
    print("\n🚫 변환 실패 파일 목록:")
    for f in failed_files:
        print(f" - {f}")
else:
    print("\n🎉 모든 mp4 → wav 변환 성공!")
