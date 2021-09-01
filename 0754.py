fin  = open("input.txt")
fout = open("output.txt","w")
 
a, b, c = map(int, fin.readline().split())

max_ves = 727
min_ves = 94

if a <= max_ves and b <= max_ves and c <= max_ves:
    if a >= min_ves and b >= min_ves and c >= min_ves:
        fout.write(str(max(a,b,c)))
    else:
        fout.write('Error')
else:
    fout.write('Error')
 
fin.close()
fout.close()