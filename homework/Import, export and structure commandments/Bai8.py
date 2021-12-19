def Bai8():
    print("Nhập vào 2 số nguyên: ")
    m = int(input("Nhập vào số m: "))
    n = int(input("Nhập vào số n: "))
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s = '*' * j
        print(s)

if __name__ == "__main__":
    Bai8()
