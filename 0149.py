fin  = open("input.txt")
fout = open("output.txt","w")


a = int(fin.readline())
i = 0
data = [int(n) for n in fin.read().split()]

for i in reversed(data):
    fout.write(str(i) + ' ')

#fout.write(str(data))
fin.close()
fout.close()