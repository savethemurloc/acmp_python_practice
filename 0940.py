fin  = open("input.txt")
fout = open("output.txt","w")

chislo, slovo = fin.readline().split()
res = ""
i = 0
chislo = int(chislo)
if chislo - 1 >= 0:
    while i < len(slovo):
        if i == chislo - 1:
            i += 1
            continue
        res += slovo[i]
        i += 1

fout.write(res)

fin.close()
fout.close()