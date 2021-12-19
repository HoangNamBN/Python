def PhepToan(a, b):
    tong = a + b
    hieu = a - b
    tich = a*b
    print("a + b = ", tong , "\na - b= ", hieu,"\na * b = ", tich)
    if b == 0:
        print("Mẫu số bằng 0")
    else:
        thuong = a/b
        print("a/b = ", thuong)

def nhapthongtin():
    print("Nhập vào 2 số a và b: ")
    while True:
        try:
            a = float(input("Nhập vào số a: "))
            b = float(input("Nhập vào số b: "))
        except ValueError:
            print("Xin vui lòng nhập vào dữ liệu kiểu float")
            continue
        else:
            break
    return a, b

if __name__ == "__main__":
    a, b = nhapthongtin()
    PhepToan(a, b)

