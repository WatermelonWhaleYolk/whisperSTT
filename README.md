<<<<<<< HEAD
# whisperSTT
=======
# Whisper

[[Blog]](https://openai.com/blog/whisper)
[[Paper]](https://cdn.openai.com/papers/whisper.pdf)
[[Model card]](model-card.md)
[[Colab example]](https://colab.research.google.com/github/openai/whisper/blob/master/notebooks/LibriSpeech.ipynb)

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification.


## Approach

![Approach](approach.png)

A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. All of these tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing for a single model to replace many different stages of a traditional speech processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets.


## Setup

We used Python 3.9.9 and [PyTorch](https://pytorch.org/) 1.10.1 to train and test our models, but the codebase is expected to be compatible with Python 3.7 or later and recent PyTorch versions. The codebase also depends on a few Python packages, most notably [HuggingFace Transformers](https://huggingface.co/docs/transformers/index) for their fast tokenizer implementation and [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) for reading audio files. The following command will pull and install the latest commit from this repository, along with its Python dependencies 

    pip install git+https://github.com/openai/whisper.git 

It also requires the command-line tool [`ffmpeg`](https://ffmpeg.org/) to be installed on your system, which is available from most package managers:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg                         

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg
```


## Available models and languages

There are five model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and relative speed. 


|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

For English-only applications, the `.en` models tend to perform better, especially for the `tiny.en` and `base.en` models. We observed that the difference becomes less significant for the `small.en` and `medium.en` models.

Whisper's performance varies widely depending on the language. The figure below shows a WER breakdown by languages of Fleurs dataset, using the `large` model. More WER and BLEU scores corresponding to the other models and datasets can be found in Appendix D in [the paper](https://cdn.openai.com/papers/whisper.pdf).

![WER breakdown by language](language-breakdown.svg)



## Command-line usage

The following command will transcribe speech in audio files, using the `medium` model:

    whisper audio.flac audio.mp3 audio.wav --model medium

The default setting (which selects the `small` model) works well for transcribing English. To transcribe an audio file containing non-English speech, you can specify the language using the `--language` option:

    whisper japanese.wav --language Japanese

Adding `--task translate` will translate the speech into English:

    whisper japanese.wav --language Japanese --task translate

Run the following to view all available options:

    whisper --help

See [tokenizer.py](whisper/tokenizer.py) for the list of all available languages.


## Python usage

Transcription can also be performed within Python: 

```python
import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

Internally, the `transcribe()` method reads the entire file and processes the audio with a sliding 30-second window, performing autoregressive sequence-to-sequence predictions on each window.

Below is an example usage of `whisper.detect_language()` and `whisper.decode()` which provide lower-level access to the model.

```python
import whisper

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("audio.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)
```

## License

<<<<<<< HEAD
The code and the model weights of Whisper are released under the MIT License. See `LICENSE` for further details.
>>>>>>> 6e3be77 (initial commit)
=======
The code and the model weights of Whisper are released under the MIT License. See [LICENSE](LICENSE) for further details.
>>>>>>> 08a739a (make LICENSE a link instead of code-formatted text)
