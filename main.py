import random

maratons = []
f = open('maratons.txt', 'w')
for _ in range(365):
    maratons.append(str(random.choices([0,1], [0.3, 0.7])[0]))
f.write(','.join(maratons))
f.close()

f = open('maratons.txt', 'r')
dati = f.read().split(',')
f.close()

skreja = dati.count('1')
periodi = 0
pauze = 0

for diena in dati:
    if diena == '0': pauze += 1
    else:
        if pauze >=4:
            periodi += 1
            pauze =0

if pauze >=4: periodi +=1

print("Dienas kad Marta devas skriet:", skreja)
print("Periodi ar vismaz 4 dienam pec kartas kad skriešana izpalika:", periodi)
