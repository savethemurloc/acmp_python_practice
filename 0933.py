fin  = open("input.txt")
fout = open("output.txt","w")
 
a, b, c, d = map(int, fin.readline().split())

if d <= a:
    res = d * b
else:
    res = (a * b) + ((d - a) * c)

fout.write(str(res))

fin.close()
fout.close()