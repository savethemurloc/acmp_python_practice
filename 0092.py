fin  = open("input.txt")
fout = open("output.txt","w")

a = int(fin.read())

if a % 2 == 0:
    fout.write(str(a // 2))
elif a == 1:
    fout.write('0')
else:
    fout.write(str(a))

fin.close()
fout.close()