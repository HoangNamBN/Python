def ptbn(a, b):
    result = ""
    if (a == 0):
        if (b == 0):
            result = "Phương trình vô số nghiệm"
        else:
            result = "Phương trình vô nghiệm"
    else:
        result = "Phương trình có nghiệm duy nhất" + str(-b / a)
    return result;


def nhapthongtin():
    while True:
        try:
            a = float(input("Nhập số a: "))
            b = float(input("nhập số b: "))
        except ValueError:
            print("Đây không phải là số, mời bạn nhập lại")
            continue
        else:
            break;
    return a, b


if __name__ == "__main__":
    a, b = nhapthongtin()
    print(ptbn(a, b))
    print("Bạn có muốn tiếp tục chạy chương trình hay không")
    while True:
        traloicauhoi = input("Nhập câu trả lời Yes/No: ")
        if (traloicauhoi == "Y"):
            try:
                c = float(input("Nhập số c: "))
                d = float(input("nhập số d: "))
                print(ptbn(c, d))
            except ValueError:
                print("Đây không phải là số, mời bạn nhập lại")
                continue
        else:
            break
