fin  = open("input.txt")
fout = open("output.txt","w")

a, b, c = map(int, fin.readline().split())

if 2*c <= a and 2*c <= b:
    fout.write('YES')
else:
    fout.write('NO')

fin.close()
fout.close()