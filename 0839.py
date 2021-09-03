fin  = open("input.txt")
fout = open("output.txt","w")

s = fin.readline()
i = 0

#print(s)

while i < len(s):
    #print(s[i])
    if s[i] != '1':
        fout.write('NO')
        break
    i += 1
    if i == len(s):
        fout.write('YES')

fin.close()
fout.close()