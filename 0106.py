fin  = open("input.txt")
fout = open("output.txt","w")

a = int(fin.readline())

data = []
for line in fin:
    data.append([int(x) for x in line.split()])


eds = 0
nols = 0
for x in data:
    if x == [0]:
        nols += 1
    else:
        eds += 1


fout.write(str(min(eds,nols)))

fin.close()
fout.close()