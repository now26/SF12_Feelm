# Vue3 & Django 프로젝트 관련 패키지들 (24.11.24. 기존 requirements.txt 기반)

## 1. Django 및 관련 패키지들 (백엔드 프레임워크)
- `Django==4.2.16`
- `django-allauth==0.61.1`
- `django-cors-headers==4.6.0`
- `django-environ==0.11.2`
- `django-extensions==3.2.3`
- `django-redis==5.4.0`
- `djangorestframework==3.15.2`
- `djangorestframework-simplejwt==5.3.1`
- `dj-rest-auth==7.0.0`

## 2. 비동기 관련 패키지들
- `asgiref==3.8.1`
- `async-timeout==5.0.1`
- `anyio==4.4.0`
- `httpcore==1.0.5`
- `httpx==0.27.0`
- `sniffio==1.3.1`
- `trio==0.27.0`
- `trio-websocket==0.11.1`

## 3. JWT 및 인증 관련 패키지들
- `PyJWT==2.10.0`
- `oauthlib==3.2.2`
- `requests-oauthlib==2.0.0`
- `python3-openid==3.2.0`
- `pytz==2024.1`

## 4. 데이터베이스 및 캐시 관련
- `redis==5.2.0`
- `sqlparse==0.5.1`
- `django-redis==5.4.0`

## 5. 보안 관련 패키지들
- `cryptography==43.0.3`
- `defusedxml==0.7.1`
- `PySocks==1.7.1`

## 6. 로깅 및 디버깅 관련
- `debugpy==1.8.2`
- `stack-data==0.6.3`
- `colorama==0.4.6`
- `click==8.1.7`

## 7. 프론트엔드 및 렌더링 관련
- `Jinja2==3.1.4`
- `Werkzeug==3.1.2`
- `MarkupSafe==3.0.2`

## 8. 데이터 처리 및 패키지들
- `pandas==2.2.2`
- `numpy==2.0.1`
- `imageio==2.36.0`
- `pillow==10.4.0`
- `pywin32==306`
- `scikit-learn==1.5.2`

## 9. CORS 관련 패키지들
- `django-cors-headers==4.6.0`

## 10. 패키지 관리 및 필수 도구들
- `attrs==24.2.0`
- `certifi==2024.8.30`
- `chardet==5.2.0`
- `charset-normalizer==3.4.0`
- `packaging==24.1`
- `platformdirs==4.2.2`
- `zipp==3.19.2`

---

# 관련 없는 패키지들

## 1. Flask 및 관련 패키지들
- `Flask==3.0.3`
- `Flask-Cors==5.0.0`
- `Flask-Login==0.6.3`

## 2. Jupyter 관련 패키지들
- `ipykernel==6.29.5`
- `ipython==8.18.1`
- `jupyter_client==8.6.2`
- `jupyter_core==5.7.2`

## 3. 웹 스크래핑 및 자동화 관련 패키지들
- `beautifulsoup4==4.12.3`
- `selenium==4.26.1`
- `pytesseract==0.3.13`

## 4. 성능 테스트 관련 패키지들
- `locust==2.32.1`

## 5. 기타 일반적인 라이브러리들
- `sympy==1.13.3`
- `Markdown==3.7`
- `markdownify==0.13.1`
- `fonttools==4.53.1`
- `cryptography==43.0.3`
- `tornado==6.4.1`
- `tqdm==4.66.4`

## 6. 데이터 처리와 관련이 있지만, 프론트엔드나 백엔드 프로젝트에서 직접 사용하지 않는 경우가 많음
- `numpy==2.0.1`
- `pandas==2.2.2`


---------------------------------------------

annotated-types==0.7.0
anyio==4.4.0
asgiref==3.8.1
asttokens==2.4.1
async-timeout==5.0.1
attrs==24.2.0
beautifulsoup4==4.12.3
blinker==1.8.2
Brotli==1.1.0
certifi==2024.8.30
cffi==1.17.1
chardet==5.2.0
charset-normalizer==3.4.0
click==8.1.7
colorama==0.4.6
comm==0.2.2
ConfigArgParse==1.7
contourpy==1.2.1
cryptography==43.0.3
cycler==0.12.1
debugpy==1.8.2
decorator==5.1.1
defusedxml==0.7.1
distro==1.9.0
dj-rest-auth==7.0.0
Django==4.2.16
django-allauth==0.61.1
django-cors-headers==4.6.0
django-environ==0.11.2
django-extensions==3.2.3
django-redis==5.4.0
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
exceptiongroup==1.2.2
executing==2.1.0
Flask==3.0.3
Flask-Cors==5.0.0
Flask-Login==0.6.3
fonttools==4.53.1
gevent==24.10.3
geventhttpclient==2.3.1
greenlet==3.1.1
h11==0.14.0
httpcore==1.0.5
httpx==0.27.0
idna==3.10
imageio==2.36.0
importlib_metadata==8.0.0
importlib_resources==6.4.0
ipykernel==6.29.5
ipython==8.18.1
itsdangerous==2.2.0
jedi==0.19.1
Jinja2==3.1.4
jupyter_client==8.6.2
jupyter_core==5.7.2
kiwisolver==1.4.5
locust==2.32.1
Markdown==3.7
markdownify==0.13.1
MarkupSafe==3.0.2
mpmath==1.3.0
msgpack==1.1.0
nest-asyncio==1.6.0
numpy==2.0.1
oauthlib==3.2.2
openai==1.35.13
outcome==1.3.0.post0
packaging==24.1
pandas==2.2.2
parso==0.8.4
pexpect==4.9.0
pillow==10.4.0
platformdirs==4.2.2
prompt_toolkit==3.0.47
psutil==6.0.0
ptyprocess==0.7.0
pure_eval==0.2.3
pycparser==2.22
pydantic==2.8.2
pydantic_core==2.20.1
Pygments==2.18.0
PyJWT==2.10.0
pyparsing==3.1.2
PySocks==1.7.1
pytesseract==0.3.13
python-dateutil==2.9.0.post0
python3-openid==3.2.0
pytz==2024.1
pywin32==306
pyzmq==26.0.3
redis==5.2.0
requests==2.32.3
requests-oauthlib==2.0.0
selenium==4.26.1
six==1.16.0
sniffio==1.3.1
sortedcontainers==2.4.0
soupsieve==2.6
sqlparse==0.5.1
stack-data==0.6.3
sympy==1.13.3
tomli==2.0.2
tornado==6.4.1
tqdm==4.66.4
traitlets==5.14.3
trio==0.27.0
trio-websocket==0.11.1
typing_extensions==4.12.2
tzdata==2024.2
urllib3==2.2.3
wcwidth==0.2.13
websocket-client==1.8.0
Werkzeug==3.1.2
Wikipedia-API==0.6.0
wsproto==1.2.0
zipp==3.19.2
zope.event==5.0
zope.interface==7.1.1