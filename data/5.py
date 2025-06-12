import transformers
from transformers import TrainingArguments
print("🔥 transformers version:", transformers.__version__)
print("🔥 TrainingArguments module:", TrainingArguments.__module__)
print("🔥 transformers location:", transformers.__file__)
# ===================================

from datasets import load_dataset, Audio
from transformers import WhisperProcessor, WhisperForConditionalGeneration, Trainer
import torch
import os

# 1. 데이터 로드 및 경로 정리
dataset = load_dataset("csv", data_files={"train": "segments_dataset.csv"}, delimiter=",")

def fix_path(example):
    example["audio"] = example["audio"].replace("\\", "/")  # 윈도우 경로 수정
    return example

dataset["train"] = dataset["train"].map(fix_path)

# 2. 오디오 컬럼 형 변환
dataset["train"] = dataset["train"].cast_column("audio", Audio(sampling_rate=16000))

# 3. 이전에 파인튜닝된 모델 불러오기
model_path = "../zeraV03"
processor = WhisperProcessor.from_pretrained(model_path)
model = WhisperForConditionalGeneration.from_pretrained(model_path)

# 4. 전처리 함수 정의
def preprocess(example):
    audio = example["audio"]["array"]
    inputs = processor.feature_extractor(audio, sampling_rate=16000)
    input_features = inputs["input_features"][0]
    labels = processor.tokenizer(example["transcription"]).input_ids
    return {
        "input_features": input_features,
        "labels": labels
    }

# 5. 전처리 실행
dataset = dataset["train"].map(preprocess)

# 6. 데이터 콜레이터 정의
def data_collator(batch):
    input_features = torch.tensor([example["input_features"] for example in batch])
    labels = [torch.tensor(example["labels"]) for example in batch]
    labels = torch.nn.utils.rnn.pad_sequence(
        labels, batch_first=True, padding_value=processor.tokenizer.pad_token_id
    )
    return {"input_features": input_features, "labels": labels}

# 7. 학습 설정
training_args = TrainingArguments(
    output_dir="../zeraV04",  # 체크포인트 저장 폴더
    per_device_train_batch_size=4,
    gradient_accumulation_steps=2,
    learning_rate=2e-5,
    warmup_steps=100,
    max_steps=6000,
    logging_steps=50,
    save_steps=2000,
    save_total_limit=2,
)

# 8. Trainer 구성
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=processor,  # ✅ 문제 해결: feature_extractor가 아닌 processor 전체 넘기기
    data_collator=data_collator,
)

# 9. 학습 실행
trainer.train()