import os
import pandas as pd

csv_path = "segments_dataset.csv"  # 현재 디렉토리 기준
df = pd.read_csv(csv_path)

for path in df["audio"]:
    if not os.path.exists(path):
        print(f"❌ 존재하지 않음: {path}")
    else:
        print(f"✅ 존재함: {path}")
