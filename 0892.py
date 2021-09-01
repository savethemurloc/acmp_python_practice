fin  = open("input.txt")
fout = open("output.txt","w")
 
a = int(fin.readline())

if a >= 3 and a <= 5:
    fout.write('Spring')
elif a >= 6 and a <= 8:
    fout.write('Summer')
elif a >= 9 and a <= 11:
    fout.write('Autumn')
elif a == 12 or a == 1 or a == 2:
    fout.write('Winter')
else:
    fout.write('Error')
 
fin.close()
fout.close()