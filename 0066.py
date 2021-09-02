fin  = open("input.txt")
fout = open("output.txt","w")
 
a = fin.readline()

alfavit = 'qwertyuiopasdfghjklzxcvbnmq'
res = alfavit.find(a[0]) + 1

fout.write(alfavit[res])

fin.close()
fout.close()