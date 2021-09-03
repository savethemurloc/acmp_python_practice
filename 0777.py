fin  = open("input.txt")
fout = open("output.txt","w")
 
s, b = map(int, fin.readline().split())
res = 0

while s != b:
    res += 1
    s += 1
    if s == 13:
        s = 1

fout.write(str(res))

fin.close()
fout.close()