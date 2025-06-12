import transformers
from transformers import TrainingArguments
import torch
from pathlib import Path
from datasets import load_dataset, Audio
from transformers import WhisperProcessor, WhisperForConditionalGeneration, Trainer

dataset = load_dataset("csv", data_files={"train": "segments_dataset.csv"}, delimiter=",")
def fix_path(example):
    example["audio"] = example["audio"].replace("\\", "/")  # 윈도우 경로 수정
    return example
dataset["train"] = dataset["train"].map(fix_path)
dataset["train"] = dataset["train"].cast_column("audio", Audio(sampling_rate=16000))

#파인튜닝 모델명 Path("모델명명")
model_path = Path("zeraV03").resolve()


processor = WhisperProcessor.from_pretrained(model_path, local_files_only=True)
model = WhisperForConditionalGeneration.from_pretrained(model_path, local_files_only=True)

def preprocess(example):
    audio = example["audio"]["array"]
    inputs = processor(audio, sampling_rate=16000, return_tensors="pt")
    input_features = inputs.input_features[0]
    labels = processor.tokenizer(
        example["transcription"], padding="longest", return_tensors="pt"
    ).input_ids[0]
    return {
        "input_features": input_features,
        "labels": labels
    }

dataset = dataset["train"].map(preprocess)

def data_collator(batch):
    input_features = torch.stack([example["input_features"] for example in batch])
    labels = [example["labels"] for example in batch]
    labels = torch.nn.utils.rnn.pad_sequence(
        labels, batch_first=True, padding_value=processor.tokenizer.pad_token_id
    )
    return {"input_features": input_features, "labels": labels}

training_args = TrainingArguments(
    output_dir=Path("zeraV04").resolve(),
    per_device_train_batch_size=4,
    gradient_accumulation_steps=2,
    learning_rate=2e-5,
    warmup_steps=100,
    max_steps=6000,
    logging_steps=50,
    save_steps=2000,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=processor,
    data_collator=data_collator,
)

# 10. 학습 실행
trainer.train()
