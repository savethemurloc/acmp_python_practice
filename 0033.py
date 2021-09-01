fin  = open("input.txt")
fout = open("output.txt","w")
 
a, b = map(int, fin.readline().split())

fout.write(str(b - 1) + ' ' + str(a - 1))
 
fin.close()
fout.close()