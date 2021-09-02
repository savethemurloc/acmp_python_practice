fin  = open("input.txt")
fout = open("output.txt","w")
 
a = fin.readline()

if a[0] == a[3] and a[1] == a[2]:
    fout.write('YES')
else:
    fout.write('NO')

fin.close()
fout.close()