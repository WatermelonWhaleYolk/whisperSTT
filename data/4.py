from datasets import load_dataset, Audio

dataset = load_dataset("csv", data_files="segments_dataset.csv", split="train")
dataset = dataset.cast_column("audio", Audio())