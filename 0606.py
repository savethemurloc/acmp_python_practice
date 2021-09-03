fin  = open("input.txt")
fout = open("output.txt","w")
 
a, b, c = map(int, fin.readline().split())

if a < b + c and b < a + c and c < a + b:
    fout.write('YES')
else:
    fout.write('NO')

fin.close()
fout.close()