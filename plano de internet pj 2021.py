#https://olimpiada.ic.unicamp.br/pratique/pj/2021/f1/plano/

q = int(input())
n_mes = int(input())
total = q * n_mes
for i in range(n_mes):
  M_i = int(input())
  total -= M_i
print(total + q)
