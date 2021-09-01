fin  = open("input.txt")
fout = open("output.txt","w")


a, b, c = map(int, fin.readline().split())

res = max(a, b, c) - min(a, b, c)

fout.write(str(res))
 
fin.close()
fout.close()