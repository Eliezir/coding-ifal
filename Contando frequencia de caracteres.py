#https://thehuxley.com/problem/2835?quizId=7580
frase = input()
letras = []
num = []
for x in range(len(frase)):
  if frase[x] not in letras:
    letras.append(frase[x])
for y in range(len(letras)):
  num.append(frase.count(letras[y]))
  print(letras[y],num[y])

#ou
#import collections
#print(collections.Counter(input()))
