def calc_area(radios) :
    global area
    area = 3.14 * radios**2
    return
area = 0
ban = float(input("반지름을 입력하세요"))
calc_area(ban)

print("면적:", area)
