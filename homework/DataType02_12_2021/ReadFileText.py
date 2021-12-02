f = open('datatxt.txt', 'r', encoding="utf8")
print("Kết quả đọc từng dòng của file dữ liệu là: \n")
i = 0
while True:
    data = f.readline()
    if data == '':
        break
    word = data.split()
    i += 1
    print("Dòng thứ " + str(i) +": " + data + "Danh sách từng từ trong câu là: ", word)
    print("\n")

f.close()

