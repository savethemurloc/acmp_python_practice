fin  = open("input.txt")
fout = open("output.txt","w")

a = int(fin.readline())

a = a ** 2

fout.write(str(a))

fin.close()
fout.close()