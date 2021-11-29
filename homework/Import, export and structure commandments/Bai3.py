import math


def isSoChinhPhuong():
    print("Nhập vào 1 số nguyên: ")
    a = float(input("Nhập vào số a: "))

    b = int(math.sqrt(a))
    if b * b == a:
        print(str(a) + " là số chính phương")
    else:
        print(str(a) + " không là số chính phương")


if __name__ == "__main__":
    isSoChinhPhuong()
