#https://olimpiada.ic.unicamp.br/pratique/p1/2021/f2/lista/
num_ele = int(input())
lista = input().split()
ope = 0
c1 = 0
c2 = num_ele-1
while c2 > c1:
  if lista[c1]!=lista[c2]:
    ope +=1
  c1+=1
  c2-=1
print(ope)
  
