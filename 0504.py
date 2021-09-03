def swap(string):
      return string[2] + string[0] + string[1]

fin  = open("input.txt")
fout = open("output.txt","w")
 
t = int(fin.readline())

res = 'GCV'
i = 0

while i < t:
    res = swap(res)
    i += 1

fout.write(res)

fin.close()
fout.close()