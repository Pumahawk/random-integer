import random, sys

num = []
minimo, massimo, tot = 0, 99, 10
rip = True


#read options
args = sys.argv

for k in range(len(args)):
    if args[k] == "-min":
        minimo = int(args[k+1])
        continue
    elif args[k] == "-max":
        massimo = int(args[k+1])
        continue
    elif args[k] == "-num":
        tot = int(args[k+1])
        continue
    elif args[k] == "-rip":
        rip = True
        continue
    elif args[k] == "-nrip":
        rip = False
        continue
        
i = 0
while i < tot:
    p = random.randint(minimo, massimo)
    if rip or p not in num:
        num.append(p)
        i = i + 1
for numero in num:
    print(numero)
