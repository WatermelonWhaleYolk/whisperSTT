from datasets import load_dataset, Audio
from transformers import WhisperProcessor, WhisperForConditionalGeneration, TrainingArguments, Trainer
import torch
import librosa

# 1. 데이터 로드 및 경로 수정
dataset = load_dataset("csv", data_files={"train": "segments_dataset.csv"}, delimiter=",")

def fix_path(example):
    example["audio"] = example["audio"].replace("\\", "/")  # 백슬래시 -> 슬래시
    return example

dataset["train"] = dataset["train"].map(fix_path)

# 2. 오디오 컬럼을 Audio 타입으로 캐스팅
dataset["train"] = dataset["train"].cast_column("audio", Audio(sampling_rate=16000))

# 3. 모델/프로세서 로딩
model_name = "openai/whisper-small"
processor = WhisperProcessor.from_pretrained(model_name)
model = WhisperForConditionalGeneration.from_pretrained(model_name)

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

# 5. 전처리 적용
dataset = dataset["train"].map(preprocess)

# 6. 데이터 콜레이터 정의
def data_collator(batch):
    input_features = torch.tensor([example["input_features"] for example in batch])
    labels = [torch.tensor(example["labels"]) for example in batch]
    labels = torch.nn.utils.rnn.pad_sequence(labels, batch_first=True, padding_value=processor.tokenizer.pad_token_id)
    return {"input_features": input_features, "labels": labels}

# 7. 학습 설정
training_args = TrainingArguments(
    output_dir="./whisper-finetuned",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=1,
    learning_rate=1e-5,
    warmup_steps=10,
    max_steps=500,
    logging_steps=10,
    save_steps=100,
    report_to="none"
)

# 8. Trainer 구성 및 학습 시작
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=processor.feature_extractor,  # 경고 무시해도 됨
    data_collator=data_collator
)

trainer.train()