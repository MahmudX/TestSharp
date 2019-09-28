f = open('D:\\Py Learning\\11. FIle IO\\sample.txt', 'rt')
o = open('D:\\Py Learning\\11. FIle IO\\output.txt', 'wt')
for line in f:
    print(line.rstrip())
    o.writelines(line)
    print(line.rstrip(), file=o)