fin  = open("input.txt")
fout = open("output.txt","w")
 
a, b, c = map(int, fin.readline().split())

a = a // 2
b = b // 6

res = min(a, b, c)

fout.write(str(res))

fin.close()
fout.close()