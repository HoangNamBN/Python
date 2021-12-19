import math
def Bai11():
    print("Nhập các hệ số a, b, c")
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình vô số nghiệm!")
            else:
                print("Phương trình vô nghiệm!")
        else:
            x1 = -c/b;
            print("Phương trình có nghiệm duy nhất x = ", x1)
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            print("Phương trình vô nghiệm!")
        elif delta == 0:
            x1 = -b/(2*a)
            print("Phương trình có nghiệm x = ", x1)
        else:
            x1 = (-b - math.sqrt(delta))/ (2*a)
            x2 = (-b + math.sqrt(delta))/ (2*a)
            print("Phương trình có 2 nghiệm phân biệt x1 = ", x1, "và nghiệm x2 = ", x2)

if __name__ == "__main__":
    Bai11()