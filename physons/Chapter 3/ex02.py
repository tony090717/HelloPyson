americano_price = 2000
latte_price = 3000
cappuccino_price = 3500



ame_cups = int(input("아메리카노의 잔수를 입력하세요."))
latte_cups = int(input("카페라떼의 잔수를 입력하세요."))
capu_cups = int(input("카푸치노의 잔수를 입력하세요."))

sum_all = 0
sum_all = americano_price * ame_cups
sum_all = sum_all + latte_price * latte_cups
sum_all = sum_all+ cappuccino_price * capu_cups


print("총매출은" +str(sum_all)+"원입니다.")
