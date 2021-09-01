fin  = open("input.txt")
fout = open("output.txt","w")
 
a = fin.read()
fout.write(a)
 
fin.close()
fout.close()