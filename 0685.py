fin  = open("input.txt")
fout = open("output.txt","w")
 
a, b, c, d, e, f = map(int, fin.readline().split())

ar_a = [a, b, c]
ar_b = [d, e, f]
res = 0
i = 0

while i < 3:
    res += max(ar_a) * max(ar_b)
    ar_a.remove(max(ar_a))
    ar_b.remove(max(ar_b))
    i += 1

fout.write(str(res))

fin.close()
fout.close()