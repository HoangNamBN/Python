import math

def Bai27():
    print("Nhập thông tin của đường tròn thứ nhất: ")
    x1 = float(input("nhập tọa độ x1: "))
    y1 = float(input("nhập tọa độ y1: "))
    R1 = float(input("nhập bán kính R1: "))

    print("Nhập thông tin của đường tròn thứ hai: ")
    x2 = float(input("nhập tọa độ x2: "))
    y2 = float(input("nhập tọa độ y2: "))
    R2 = float(input("nhập bán kính R2: "))

    khoangCach = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    if khoangCach == R1 +R2 or khoangCach == math.fabs(R1 - R2):
        print("Hai đường tròn tiếp xúc!")
    else:
        print("2 đường tròn không tiếp xúc nhau")

if __name__ == "__main__":
    Bai27()