#https://thehuxley.com/problem/2910?locale=pt_BR
doces = int(input())
evolucoes = 0

pokemons = []
for x in range(3): 
  pokemons.append(int(input()))
pokemons.sort()
for x in range(3):
  if doces > pokemons[x]:
    doces -= pokemons[x]
    evolucoes = x +1
  else :
    break
print(evolucoes)

  

