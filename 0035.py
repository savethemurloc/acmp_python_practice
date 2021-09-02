fin  = open("input.txt")
fout = open("output.txt","w")
 
a = int(fin.readline())
res = []
i = 0

while i < a:
    n, m = map(int, fin.readline().split())
    res.append( (19*m) + ( ( n + 239 ) * ( n + 366 ) // 2 ) )
    i += 1

for f in res:
    fout.write(str(f) + "\n")

fin.close()
fout.close()