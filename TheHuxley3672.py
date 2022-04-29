#https://thehuxley.com/problem/3672

cpfs = []
notas = []
inscritos = int(input())
for i in range(inscritos):
  cpf = int(input())
  cpfs.append(cpf)
for x in range(inscritos):
  nota = int(input())
  notas.append(nota)

i = 0
f = inscritos-1
inicio = i
fim = f
pesquisa = int(input())

cpfs_busca = []

for z in range(pesquisa): 
  cpfs_busca.append(int(input()))

indice = 0



while(pesquisa != indice):
  meio =(inicio+fim)//2
  chute = cpfs[meio]
  if(chute==cpfs_busca[indice]):
    print(notas[meio])
    indice+=1
    inicio = i
    fim = f
  elif(inicio >= fim):
    print("NAO SE APRESENTOU")
    indice+=1
    inicio = i
    fim = f
  elif(chute>cpfs_busca[indice]):
    fim = meio-1
  elif(chute<cpfs_busca[indice]):
    inicio = meio+1
