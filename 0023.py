fin  = open("input.txt")
fout = open("output.txt","w")
 
t = int(fin.readline())

i = 1
res = 0
while i <= t:
    if t % i == 0:
        res += i
    i += 1

fout.write(str(res))

fin.close()
fout.close()