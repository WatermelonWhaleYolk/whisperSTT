1. 2022년 9월에 출시됨

2. tiny, base, small, medium, large, turbo 총 6가지의 모델을 제공

3. 영어 전용이고 다국어 버전도 지원

4. 성별과 나이 등을 추론하는 용도로는 적절하지 않음

5. 의사결정 기반 시스템에는 부적절

6. 68만 시간의 데이터를 웹에서 수집했음

7. 98개 언어 포함

기초 설정() {
pip install -r
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
choco install ffmpeg
pip install git+https://github.com/openai/whisper.git
pip install pytest
pip uninstall torch torchvision torchaudio -y (GPU가 CUDA 지원할 경우)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118(마찬가지)

}

실행방법() {

1. data/A의 B 폴더에 mp4파일, C 폴더에 json파일 넣기(각 mp4파일과 json파일은 1대1)
2. 1에서 6.py 순서대로 실행 (경로 이상하면 학습하는 척만 할 수 있으니 root.py로 경로 확인)
3. save_model.py로 학습한 것들을 모델로 만듬
4. whisper-finetuned-final 폴더 생성
   }
