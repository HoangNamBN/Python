import re
import string

s = str(input("Nhập vào xâu s: "))
if len(s) == 0:
    print("Xâu là xâu rỗng!")
else:
    s = s.strip()
    s = re.sub(r"\s\s+", " ", s)
    print("Chuỗi sau khi viết hoa chữ cái đầu là: ", string.capwords(s))