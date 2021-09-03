fin  = open("input.txt")
fout = open("output.txt","w")

N = int(fin.readline())
data = [int(n) for n in fin.read().split()]

fout.write(str(min(data)) + ' ' + str(max(data)))

fin.close()
fout.close()