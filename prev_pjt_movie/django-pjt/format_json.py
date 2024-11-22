import json

# 기존 JSON 파일 열기 (경로 수정)
with open('accounts/fixtures/users.json', 'r') as file:
    data = json.load(file)

# 예쁘게 포맷팅하여 새로운 파일로 저장
with open('accounts/fixtures/pretty_users.json', 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
