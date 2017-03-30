remaining = open(r'D:\downloads\remaining.txt', 'r')
left = []
for a in remaining:
    temp = a.split('|')
    left.append(temp[1])
fullList = open(r'D:\downloads\list.txt', 'r')
target = open(r'D:\downloads\sortable free agent list.txt', 'a')
last = []
for a in fullList:
    temp = a.split(',')
    for b in left:
        if temp[1] == b:
            target.write(a)



