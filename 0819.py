fin  = open("input.txt")
fout = open("output.txt","w")
 
a, b, c = map(int, fin.readline().split())

V = a * b * c
S = 2 * (a * b + b * c + a * c)

fout.write(str(S) + ' ' + str(V))

fin.close()
fout.close()