fin  = open("input.txt")
fout = open("output.txt","w")

k, n = map(int, fin.readline().split())
res = 0
i = 0

while i < n:
    i += k
    res += 1
    if i >= n:
        fout.write(str(res) + " " + str(n - (i - k)))
        break
        
fin.close()
fout.close()