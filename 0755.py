fin  = open("input.txt")
fout = open("output.txt","w")

a, b, c= map(int, fin.readline().split())

res = a + b - c

if res < 0:
    fout.write('Impossible')
else:
    fout.write(str(res))   

fin.close()
fout.close()