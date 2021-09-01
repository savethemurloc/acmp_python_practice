fin  = open("input.txt")
fout = open("output.txt","w")
 
a, b = map(int, fin.readline().split())

res = a * b * a

fout.write(str(res))
 
fin.close()
fout.close()