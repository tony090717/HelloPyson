num = int(input("정수를 입력하세요."))

if num >100 or num<0 :
    print("성적을 잘못 입력하였습니다.")
elif num >=90 :
    print("a학점입니다.")
    print("축하합니다.")
elif num >= 80 :
    print("b학점입니다.")
    print("축하합니다.")
elif num >= 70 :
    print("c학점입니다.")
elif num >= 60 :
    print("d학점입니다.")
else :
    print("f.학점입니다.")
print("꿈의학교.")
