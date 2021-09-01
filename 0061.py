fin  = open("input.txt")
fout = open("output.txt","w")

first = 0
second = 0

a, b = map(int, fin.readline().split())
first += a
second += b

a, b = map(int, fin.readline().split())
first += a
second += b

a, b = map(int, fin.readline().split())
first += a
second += b

a, b = map(int, fin.readline().split())
first += a
second += b

if first > second:
    fout.write('1') 
elif second > first:
    fout.write('2')
else:
    fout.write('DRAW')   

fin.close()
fout.close()