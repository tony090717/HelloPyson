username = "dream"
passward = "1234"
while True :
    name = input("ID를 입력하세요")
    pwd = input("암호를 입력하세요")
    if username == name and passward == pwd:
        print("로그인 성공")
        break
    else:
        print("ID 또는 암호가 필요합니다.")
