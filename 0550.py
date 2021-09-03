def vivodvis(god, fout):
    data = '12/09/' 
    if god > 0 and god < 10:
        fout.write(data+'000'+str(god))
    elif god > 9 and god < 100:
        fout.write(data+'00'+str(god))
    elif god > 99 and god < 1000:
        fout.write(data+'0'+str(god))
    else:
        fout.write(data+str(god))


def vivodnonvis(god, fout):
    data = '13/09/' 
    if god > 0 and god < 10:
        fout.write(data+'000'+str(god))
    elif god > 9 and god < 100:
        fout.write(data+'00'+str(god))
    elif god > 99 and god < 1000:
        fout.write(data+'0'+str(god))
    else:
        fout.write(data+str(god))

fin  = open("input.txt")
fout = open("output.txt","w")

god = int(fin.readline())

if god % 400 == 0:
    vivodvis(god, fout)
elif god % 100 != 0:
    if god % 4 == 0:
        vivodvis(god, fout)
    else:
        vivodnonvis(god, fout)
else:
    vivodnonvis(god, fout)

fin.close()
fout.close()