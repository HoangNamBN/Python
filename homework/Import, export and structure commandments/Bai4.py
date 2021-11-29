def Bai4():
   n = int(input("Nhập vào số nguyên n = "))
   tong = 0
   dem = 0
   for i in range(2, n+1, 2):
       tong += i
       dem += 1
   if dem > 0:
       print("Tổng = ", tong/dem)
   else:
       print("không có số chẵn")

if __name__ == "__main__":
    Bai4()

