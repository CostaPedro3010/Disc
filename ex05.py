from math import sqrt

L = [9, 3, 5, 7, 2, 1]
menor = min(L)
maior = max(L)
media_geo = sqrt(menor * maior)
print(f"Lista: {L}")
print(f"Média geométrica entre {menor} e {maior} = {media_geo}.")