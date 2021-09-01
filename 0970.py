fin  = open("input.txt")
fout = open("output.txt","w")

a, b, c = map(int, fin.readline().split())

if a + b == c:
    fout.write('YES')
elif b + c == a:
    fout.write('YES')
elif a + c == b:
    fout.write('YES')
else:
    fout.write('NO')


fin.close()
fout.close()