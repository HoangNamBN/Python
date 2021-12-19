def Bai13():
    print("Nhập hai cạnh a, b")
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    if a > 0 and b > 0 and a == b:
        print("Thỏa mãn độ dài 2 cạnh hình vuông!")
        chuvi = 4 * a
        dientich = a * a
        print("Chu vi hình tam giác là ", chuvi, " và diện tích tam giác là: ", dientich)
    else:
        print("Không thỏa mãn là hình vuông!")


if __name__ == "__main__":
    Bai13()
