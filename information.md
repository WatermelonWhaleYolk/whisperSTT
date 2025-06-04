1. 2022년 9월에 출시됨

2. tiny부터 large까지 총 9개의 모델을 제공

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
}

테스트 폴더로 테스트 방법
test_transcribe.py의 모델 지정하기
@pytest.mark.parametrize('model_name', whisper.available_models())
def test_transcribe(model_name: str): 
    model = whisper.load_model(model_name).cuda()
    audio_path = os.path.join(os.path.dirname(__file__), "jfk.flac")의

whisper.available_model() 부분에 모델 입력
예시 : ["tiny"]
tiny, base, small, medium, large
pytest test/

실행방법() {
  루트 디렉토리에 실행 파일 생성
}