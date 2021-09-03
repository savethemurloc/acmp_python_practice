import math
fin  = open("input.txt")
fout = open("output.txt","w")
 
n, m, a = map(int, fin.readline().split())

res = math.ceil((m * a * 2 + n * a * 2) / 16)

fout.write(str(res))

fin.close()
fout.close()