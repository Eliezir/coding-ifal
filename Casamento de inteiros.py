#https://olimpiada.ic.unicamp.br/pratique/p1/2021/f3/casamento/
x = list(input())
y = list(input())

while len(x)!=len(y):
  if len(x)<len(y):
    x.insert(0,0)
  else:
    y.insert(0,0)
resultado1= []
resultado2= []

for n in range(len(x)):
  if int(x[n])>=int(y[n]):
    resultado1.append(x[n])
  if int(y[n])>=int(x[n]):
    resultado2.append(y[n])

r1 = ''.join(char for char in resultado1)
r2 = ''.join(char for char in resultado2)

if r1 == '':
  r1=-1
elif r2=='':
  r2 =-1

r1 = int(r1)
r2 = int(r2)
if r1<=r2:
  print(r1, r2)
else:
 print(r2, r1) 
