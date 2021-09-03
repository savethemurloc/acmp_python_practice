fin  = open("input.txt")
fout = open("output.txt","w")
 
t, tcond = fin.readline().split()
a = fin.readline()

if a == 'freeze':
    fout.write(str(min(t, tcond)))
elif a == 'heat':
    fout.write(str(max(t, tcond)))
elif a == 'auto':
    fout.write(str(tcond))
elif a == 'fan':
    fout.write(str(t))


fin.close()
fout.close()