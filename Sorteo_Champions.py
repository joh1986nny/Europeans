import random
import time
time.sleep(2)
print("###################################################")
print("#   L I G A   I N T E R N A   E U R O P E A N S   #")
print("###################################################")
time.sleep(2)
print('\n')
print("Bienvenidos a todos a los sorteos de grupos para CHAMPIONS y UEFA. Primero comenzaremos con el sorteo de CHAMPIONS y posteriormente con UEFA.")
print('\n')
time.sleep(8)
print("Comienza el sorteo de CHAMPIONS...")
time.sleep(3)
#Listas con los nombres de los 24 equipos
Campeones=["JRC25","Prosi20","Naynoa","Yerito27"] 
Puestos5al8=["Javitortas","Jonyoa9","Jam","CNPero"]
Puestos9al12=["Kofy","Jarley1","Jibu","Supino"]
Puestos13al16=["Rulovich","Pikisi","Aniakenda","Loures"]
Puestos17al20=["TBM","JMJ","Bierzo","Mascaras"]
Ascendidos=["Tonikevicius13","Kaiser1985","Escamoxador","Maikelnaight"]

print("Poniendo las bolas en los bombos y removiendo....")
time.sleep(3)
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

print("Vamos alla con el Sorteo ........ Suerte a todos.")
print('\n')
time.sleep(3)
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

time.sleep(3)
print("GRUPO B")
print("-------")
print(GrupoB[0])
print(GrupoB[1])
print(GrupoB[2])
print(GrupoB[3])
print(GrupoB[4])
print(GrupoB[5])
print('\n')

time.sleep(3)
print("GRUPO C")
print("-------")
print(GrupoC[0])
print(GrupoC[1])
print(GrupoC[2])
print(GrupoC[3])
print(GrupoC[4])
print(GrupoC[5])
print('\n')

time.sleep(3)
print("GRUPO D")
print("-------")
print(GrupoD[0])
print(GrupoD[1])
print(GrupoD[2])
print(GrupoD[3])
print(GrupoD[4])
print(GrupoD[5])
print('\n')
time.sleep(3)

print("Finaliza el sorteo de CHAMPIONS ..... En breve procederemos al sortero de UEFA.")
print('\n')
time.sleep(5)

print("Comienza el sorteo de UEFA...")
time.sleep(3)
#Listas con los nombres de los 24 equipos
Descendidos=["Ivaxavi90","Sayshyos","ManiGarcia","Perydpp"]
Puestos29a32=["Superpops","Pinseque","Espein","Juanxuvenilteis"]
Puestos33al36=["Malili","Solanitos","Seroca","Crusaider66"]
Puestos37al40=["Pedrosuarez11","Jaruru","Erwati","Vancarls"]
Puestos41al44=["Darder","Laboral","Topete","Yerayone3"]
Puestos45al48=["Thai","Morti2","Srwatson27","Davidlsm"]

print("Poniendo las bolas en los bombos y removiendo....")
time.sleep(3)
#Realiza el sorteo por ordenacion de las listas
Uefabombo1=random.sample(Descendidos,4)
Uefabombo2=random.sample(Puestos29a32,4)
Uefabombo3=random.sample(Puestos33al36,4)
Uefabombo4=random.sample(Puestos37al40,4)
Uefabombo5=random.sample(Puestos41al44,4)
Uefabombo6=random.sample(Puestos45al48,4)

#Emparejamos los resultados del paso anterior
UefaGrupoA=[Uefabombo1[0],Uefabombo2[0],Uefabombo3[0],Uefabombo4[0],Uefabombo5[0],Uefabombo6[0]]
UefaGrupoB=[Uefabombo1[1],Uefabombo2[1],Uefabombo3[1],Uefabombo4[1],Uefabombo5[1],Uefabombo6[1]]
UefaGrupoC=[Uefabombo1[2],Uefabombo2[2],Uefabombo3[2],Uefabombo4[2],Uefabombo5[2],Uefabombo6[2]]
UefaGrupoD=[Uefabombo1[3],Uefabombo2[3],Uefabombo3[3],Uefabombo4[3],Uefabombo5[3],Uefabombo6[3]]

print("Vamos alla con el Sorteo ........ Suerte a todos.")
print('\n')
time.sleep(3)

#Imprime los reusltados en Tablas
print("Grupo A")
print("-------")
print(UefaGrupoA[0])
print(UefaGrupoA[1])
print(UefaGrupoA[2])
print(UefaGrupoA[3])
print(UefaGrupoA[4])
print(UefaGrupoA[5])
print('\n')

time.sleep(3)
print("Grupo B")
print("-------")
print(UefaGrupoB[0])
print(UefaGrupoB[1])
print(UefaGrupoB[2])
print(UefaGrupoB[3])
print(UefaGrupoB[4])
print(UefaGrupoB[5])
print('\n')

time.sleep(3)
print("Grupo C")
print("-------")
print(UefaGrupoC[0])
print(UefaGrupoC[1])
print(UefaGrupoC[2])
print(UefaGrupoC[3])
print(UefaGrupoC[4])
print(UefaGrupoC[5])
print('\n')

time.sleep(3)
print("Grupo D")
print("-------")
print(UefaGrupoD[0])
print(UefaGrupoD[1])
print(UefaGrupoD[2])
print(UefaGrupoD[3])
print(UefaGrupoD[4])
print(UefaGrupoD[5])
print('\n')
time.sleep(3)

print("Hasta aqui los sorteos de CHAMPIONS y UEFA. A continuación dejamos un resumen de los grupos en ambas competiciones.")
time.sleep(5)
print('\n')

#Imprime los reusltados en lista de Champions
print("Grupos CHAMPIONS:")
print("Grupo A: ",GrupoA[0],",",GrupoA[1],",",GrupoA[2],",",GrupoA[3],",",GrupoA[4],",",GrupoA[5] )
print("Grupo B: ",GrupoB[0],",",GrupoB[1],",",GrupoB[2],",",GrupoB[3],",",GrupoB[4],",",GrupoB[5] )
print("Grupo C: ",GrupoC[0],",",GrupoC[1],",",GrupoC[2],",",GrupoC[3],",",GrupoC[4],",",GrupoC[5] )
print("Grupo D: ",GrupoD[0],",",GrupoD[1],",",GrupoD[2],",",GrupoD[3],",",GrupoD[4],",",GrupoD[5] )
print('\n')

#Imprime los reusltados en lista de la Uefa
print("Grupos UEFA:")
print("Grupo A: ",UefaGrupoA[0],",",UefaGrupoA[1],",",UefaGrupoA[2],",",UefaGrupoA[3],",",UefaGrupoA[4],",",UefaGrupoA[5] )
print("Grupo B: ",UefaGrupoB[0],",",UefaGrupoB[1],",",UefaGrupoB[2],",",UefaGrupoB[3],",",UefaGrupoB[4],",",UefaGrupoB[5] )
print("Grupo C: ",UefaGrupoC[0],",",UefaGrupoC[1],",",UefaGrupoC[2],",",UefaGrupoC[3],",",UefaGrupoC[4],",",UefaGrupoC[5] )
print("Grupo D: ",UefaGrupoD[0],",",UefaGrupoD[1],",",UefaGrupoD[2],",",UefaGrupoD[3],",",UefaGrupoD[4],",",UefaGrupoD[5] )
print('\n')

print("Nos vemos la próxima temporada.")
