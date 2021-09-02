fin  = open("input.txt")
fout = open("output.txt","w")
 
a, b = map(int, fin.readline().split())

res = (a - 1) * (b - 1)


fout.write(str(res))

fin.close()
fout.close()