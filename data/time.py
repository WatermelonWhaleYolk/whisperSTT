import os
import wave
import datetime

def get_wav_duration(path):
    with wave.open(path, 'rb') as wav:
        frames = wav.getnframes()
        rate = wav.getframerate()
        return frames / float(rate)

def seconds_to_hms(seconds):
    return str(datetime.timedelta(seconds=int(seconds)))

# time.py 기준 상대 경로
b_folder_path = os.path.join("A", "B")

total_duration = 0.0
total_size_bytes = 0

for filename in os.listdir(b_folder_path):
    if filename.lower().endswith(".wav"):
        full_path = os.path.join(b_folder_path, filename)
        total_duration += get_wav_duration(full_path)
        total_size_bytes += os.path.getsize(full_path)

# 출력
print("전체 재생 시간 합계:", seconds_to_hms(total_duration))

# 바이트 → 메가바이트로 변환 (소수점 둘째자리까지)
total_size_mb = total_size_bytes / (1024 * 1024)
print("전체 용량 합계: {:.2f} MB".format(total_size_mb))
