def docfile():
    with open('datatxt.txt', 'r', encoding='UTF-8') as rf:
        line = rf.readline()
        index = 1
        while line:
            print('Line {}: {}'.format(index, line))
            index += 1
            line = rf.readline()
docfile()