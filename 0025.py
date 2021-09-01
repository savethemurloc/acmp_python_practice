fin  = open("input.txt")
fout = open("output.txt","w")
 
a = int(fin.readline())
b = int(fin.readline())

if a < b:
    res = "<"
elif a > b:
    res = ">"
else:
    res = "="

fout.write(res)
 
fin.close()
fout.close()