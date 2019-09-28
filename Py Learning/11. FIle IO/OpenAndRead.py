f = open('sample.txt', 'rt')
o = open('output.txt', 'wt')
for line in f:
    print(line.rstrip())
    o.writelines(line)
    # print(line.rstrip(), file=o)
