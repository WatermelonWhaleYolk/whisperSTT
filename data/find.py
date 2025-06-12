import os

# A_path를 상대 경로로 설정
A_path = os.path.join("Desktop", "whisperSTT", "data", "A")
B_path = os.path.join(A_path, "B")
C_path = os.path.join(A_path, "C")

missing_mp4 = []

for json_file in os.listdir(C_path):
    if json_file.endswith(".json"):
        base = os.path.splitext(json_file)[0]
        mp4_path = os.path.join(B_path, f"{base}.mp4")
        if not os.path.exists(mp4_path):
            missing_mp4.append(base + ".mp4")

if missing_mp4:
    print("❌ 다음 mp4 파일이 존재하지 않음:")
    for filename in missing_mp4:
        print(" -", filename)
else:
    print("✅ 모든 json에 대응하는 mp4 파일이 존재함.")
