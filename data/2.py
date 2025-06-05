import pandas as pd
import ast

df = pd.read_csv("train.csv")

def extract_path(audio_cell):
    try:
        audio_dict = ast.literal_eval(audio_cell)
        return audio_dict.get("path", "").replace("\\", "/")
    except Exception:
        return None

# 오디오 경로 정리
df["audio"] = df["audio"].apply(extract_path)

# 외국어 발화 같은 불필요한 전사 제거
df = df[~df["transcription"].str.contains("&외국어 발화&|@이름", regex=True, na=False)]

# NaN 제거
df = df.dropna()

# 저장
df.to_csv("cleaned_dataset.csv", index=False)
