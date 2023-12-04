l1 = [2,3,4]

l1.append(6) # [2,3,4,5,6]
print(l1[1])
print(len(l1)) # 4

l1[2] = 10 #[2,3,10,6]
del l1[2] # [2,3,6]

print(l1[-1]) #6
print(l1[-2]) #3

fajlnev = "input.txt"
f = open(fajlnev, "r") #read
sorok = f.readlines()
f.close

for i in range(len(sorok)):
    sorok[i] = sorok[i].strip()
print(sorok[0])

sum = int(sorok[1]) + int(sorok[2])
print(sum)

print(sorok)