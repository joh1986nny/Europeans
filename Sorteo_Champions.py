import random

#Listas con los nombres de los 24 equipos
Campeones=['Pauferrer','Jonyoa9','Aniakenda','Loures'] 
Puestos5al8=["Mascaras", "TBM", "JRC25", "JMJ"]
Puestos9al12=["Rulovich", "Ivaxavi90", "Jam", "CNPero"]
Puestos13al16=["Yerito27", "Jarley1",  "Kofy", "Sayshyos"]
Puestos17al20=["Mifersan", "Naynoa", "Prosi20", "Javitortas"]
Ascendidos=["Supino", "Pikisi", "Bierzo", "Jibu"]

#Realiza el sorteo por ordenacion de las listas
bombo1=random.sample(Campeones,4)
bombo2=random.sample(Puestos5al8,4)
bombo3=random.sample(Puestos9al12,4)
bombo4=random.sample(Puestos13al16,4)
bombo5=random.sample(Puestos17al20,4)
bombo6=random.sample(Ascendidos,4)

#Emparejamos los resultados del paso anterior
GrupoA=[bombo1[0],bombo2[0],bombo3[0],bombo4[0],bombo5[0],bombo6[0]]
GrupoB=[bombo1[1],bombo2[1],bombo3[1],bombo4[1],bombo5[1],bombo6[1]]
GrupoC=[bombo1[2],bombo2[2],bombo3[2],bombo4[2],bombo5[2],bombo6[2]]
GrupoD=[bombo1[3],bombo2[3],bombo3[3],bombo4[3],bombo5[3],bombo6[3]]

#Imprime los reusltados en lista
#print("Grupo A: ",GrupoA[0],GrupoA[1],GrupoA[2],GrupoA[3],GrupoA[4],GrupoA[5] )
#print("Grupo B: ",GrupoB[0],GrupoB[1],GrupoB[2],GrupoB[3],GrupoB[4],GrupoB[5] )
#print("Grupo C: ",GrupoC[0],GrupoC[1],GrupoC[2],GrupoC[3],GrupoC[4],GrupoC[5] )
#print("Grupo D: ",GrupoD[0],GrupoD[1],GrupoD[2],GrupoD[3],GrupoD[4],GrupoD[5] )
#print('\n')

#Imprime los reusltados en Tablas
print("GRUPO A")
print("-------")
print(GrupoA[0])
print(GrupoA[1])
print(GrupoA[2])
print(GrupoA[3])
print(GrupoA[4])
print(GrupoA[5])
print('\n')

print("GRUPO B")
print("-------")
print(GrupoB[0])
print(GrupoB[1])
print(GrupoB[2])
print(GrupoB[3])
print(GrupoB[4])
print(GrupoB[5])
print('\n')

print(" GRUPO C")
print("-------")
print(GrupoC[0])
print(GrupoC[1])
print(GrupoC[2])
print(GrupoC[3])
print(GrupoC[4])
print(GrupoC[5])
print('\n')

print("GRUPO D")
print("-------")
print(GrupoD[0])
print(GrupoD[1])
print(GrupoD[2])
print(GrupoD[3])
print(GrupoD[4])
print(GrupoD[5])