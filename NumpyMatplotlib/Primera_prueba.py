import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats

#Leer datos
df=pd.read_csv("dataset-act4.csv", header= 0)
print(df)

#Generar una tabla
tab2 = pd.crosstab(index=df["velocidad"],columns="Frecuencia")

tab3 = pd.crosstab(index=df["color"],columns="Frecuencia")
D1 = tab3.loc[tab3.index=="Amarillo"]
X=D1["Frecuencia"]
X = int(X)
D2 = tab3.loc[tab3.index=="Blanco"]
X2=D2["Frecuencia"]
X2 = int(X2)
D3 = tab3.loc[tab3.index=="Verde"]
X3=D3["Frecuencia"]
X3 = int(X3)

frecuencia=[D1, D2, D3]

colores = ["Amarillo", "Blanco", "Verde"]

fig, ax = plt.subplots()
ax.set_ylabel('Cantidad')
ax.set_title('Colores')
plt.bar(colores, frecuencia,color=['yellow','gray','green'])
plt.savefig('graficaFA.png')
plt.show()

T1 = D1/3
T1 = int(T1)
T2 = D2/3
T2 = int(T2)
T3 = D3/3
T3 = int(T3)

FR = [T1, T2, T3]

plt.pie(FR,labels=["Amarillo","Blanco", "Verde"],autopct="%1.1f%%",colors=['','',''])
plt.xlabel("Colores")
plt.savefig("FR.png")
plt.show()
#Punto 3 Mostrar...

peso = df["peso"]
sumaP = sum(peso)
Long = float(len(peso))
Pro = sumaP/ Long
print("Promedio de la columna peso es: ", Pro)
Lista = peso.values.tolist()
print("La mediana de la columna Altura es: ",stats.median(Lista))