f = open('data.txt', 'r', encoding="utf8")
str = f.read()
lines = str.split(".")
print(lines)
for line in lines:
    line = line.split()
    print(line)