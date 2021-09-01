fin  = open("input.txt")
fout = open("output.txt","w")
 
a = int(fin.read())
i = 0
while i < 15:
    if 2 ** i == a:
        fout.write('YES')
        break
    i += 1

if i == 15:
    fout.write('NO')

fin.close()
fout.close()