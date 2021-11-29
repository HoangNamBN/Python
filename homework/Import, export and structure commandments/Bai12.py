import math


def Bai12():
    print("Nhập ba cạnh a, b, c của tam giác")
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and c + b > a:
        print("Thỏa mãn là tam giác!")
        chuvi = a + b + c
        p = chuvi / 2
        dientich = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Chu vi hình tam giác là ", chuvi, " và diện tích tam giác là: ", dientich)
    else:
        print("Không thỏa mãn là tam giác!")


if __name__ == "__main__":
    Bai12()
