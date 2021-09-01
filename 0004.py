fin  = open("input.txt")
fout = open("output.txt","w")


a = int(fin.read())

third = 9 - a

fout.write(str(a) + '9' + str(third))
 
fin.close()
fout.close()