#https://br.spoj.com/problems/BIT/
notas = [50,10,5,1]
valor_s= []
n = 0
teste = 0
while True:
  saque=int(input())
  if saque == 0:
    break
  else:
    while saque>0:
      cedulas = saque//notas[n]
      valor_s.append(cedulas)
      saque -= cedulas*notas[n]
      n+=1
    teste +=1
    print("teste",teste)
    print(valor_s)
    print("")
    n = 0
    valor_s=[]

  
