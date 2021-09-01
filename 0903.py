fin  = open("input.txt")
fout = open("output.txt","w")
 
a = fin.read()
fout.write(str(int(a) + 1))
 
fin.close()
fout.close()