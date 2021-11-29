def Bai22():
    Fn = 0
    n = int(input("Nhập số nguyên n: "))
    if n <= 0:
        print("F(" + str(n) + ") = 0")
    else:
        ts = 1
        ms = 1
        for i in range(1, n + 1):
            ts = ts *2
            ms = ms * i
            Fn = Fn + float(ts/ms)
        print("F(" + str(n) + ") = "+ str(Fn))
if __name__ == "__main__":
    Bai22()