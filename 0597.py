fin  = open("input.txt")
fout = open("output.txt","w")


a, b, c = map(int, fin.readline().split())

if b + c <= a:
    fout.write('YES')
else:
    fout.write('NO')
fin.close()
fout.close()