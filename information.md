<ul>
<li>pip install -r</li>
<li>Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))</li>
<li>choco install ffmpeg</li>
<li>pip install git+https://github.com/openai/whisper.git</li>
<li>pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118(마찬가지)</li>
</ul>
<hr>
<ul>
<ol>data/A의 B 폴더에 mp4파일, C 폴더에 json파일 넣기(각 mp4파일과 json파일은 1대1)</ol>
<ol>1에서 6.py 순서대로 실행 (경로 이상하면 학습하는 척만 할 수 있으니 root.py로 경로 확인)</ol>
<ol>save_model.py로 학습한 것들을 모델로 만듬</ol>
<ol>whisper-finetuned-final 폴더 생성</ol>
</ul>

<ul>
<li>path.py -> 만들어진 csv파일의 내용 중 경로가 올바른지 검증</li>
<li>find.py -> 받아온 mp4파일과 json파일이 서로 대응되는지 확인</li>
<li>time.py -> B폴더에 생성된 wav파일들의 총 시간의 합 계산</li>
<li></li>
<li></li>
</ul>