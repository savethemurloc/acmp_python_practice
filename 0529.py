fin  = open("input.txt")
fout = open("output.txt","w")
 
x1, y1, x2, y2 = map(int, fin.readline().split())
res = 0

res = ( y2 - y1 ) ** 2 + ( x2 - x1 ) ** 2
res = res ** 0.5

fout.write(str(res))

fin.close()
fout.close()