x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
subx = x1-x2
suby = y1-y2
subx_2= (subx)**2
suby_2= (suby)**2
answ = (subx_2 + suby_2)**0.5
print("두점 사이의 거리=", answ)