fin  = open("input.txt")
fout = open("output.txt","w")

N = int(fin.readline())
counter = 0
data = [int(n) for n in fin.read().split()]
heig = 437

for i in data:
    counter += 1
    if i <= heig:
        fout.write("Crash " + str(counter))
        break
    if counter == N:
        fout.write("No crash")    

fin.close()
fout.close()