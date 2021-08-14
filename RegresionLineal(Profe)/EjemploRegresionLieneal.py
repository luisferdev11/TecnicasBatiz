# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:37:21 2019

@author: KIKA
"""
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

plt.rcParams['figure.figsize'] = (10, 5)
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

# cargamos los datos de entrada
data = pd.read_csv("articulos_ml.csv")
# veamos cuantas dimensiones y registros contiene
print(data.shape)

print(data.head())
print(data.describe())

# Visualizamos rápidamente las caraterísticas de entrada
# data.drop(['Title','url', 'Elapsed days'],1).hist()
# plt.show()

# Vamos a RECORTAR los datos en la zona donde se concentran más los puntos
# esto es en el eje X: entre 0 y 3.500
# y en el eje Y: entre 0 y 80.000
filtered_data = data[(data['Word count'] <= 3500) & (data['# Shares'] <= 80000)]

colores = ['orange', 'blue']
tamanios = [30, 60]

# Se crean arreglos numPy del dataset
f1 = filtered_data['Word count'].values
f2 = filtered_data['# Shares'].values

# Vamos a pintar en colores los puntos por debajo y por encima de la media de Cantidad de Palabras
asignar = []
for index, row in filtered_data.iterrows():
    if (row['Word count'] > 1808):
        asignar.append(colores[0])
    else:
        asignar.append(colores[1])

# Se dibuja el diagrama de dispersión
plt.scatter(f1, f2, c=asignar, s=tamanios[0])
#plt.show()

# Asignamos nuestra variable de entrada X para entrenamiento y las etiquetas Y.
dataX = filtered_data[["Word count"]]
X_train = np.array(dataX)
y_train = filtered_data['# Shares'].values

# Creamos el objeto de Regresión Linear
regr = linear_model.LinearRegression()

# Entrenamos nuestro modelo
regr.fit(X_train, y_train)

# Hacemos las predicciones que en definitiva una línea (en este caso, al ser 2D)
y_pred = regr.predict(X_train)

# Veamos los coeficienetes obtenidos, En nuestro caso, serán la Tangente
print('Coefficients: \n', regr.coef_)
# Este es el valor donde corta el eje Y (en X=0)
print('Independent term: \n', regr.intercept_)
# Error Cuadrado Medio
print("Mean squared error: %.2f" % mean_squared_error(y_train, y_pred))
# Puntaje de Varianza. El mejor puntaje es un 1.0
print('Variance score: %.2f' % r2_score(y_train, y_pred))


# Función Lineal.
def f(x):
    return regr.coef_ * x + 11200


x = range(0, 3000)

plt.plot(x, [f(i) for i in x])

# Establecemos el color de los ejes.
plt.axhline(0, color="black")
plt.axvline(0, color="black")

# Especificamos los limites de los ejes.
plt.xlim(0, 3000)
plt.ylim(0, 80000)

# Mostramos el gráfico.

plt.show()
# Vamos a comprobar:
# Quiero predecir cuántos "Shares" voy a obtener por un artículo con 2.000 palabras,
# según nuestro modelo, hacemos:
y_Dosmil = regr.predict([[2000]])
print("Shares predecidos: ", int(y_Dosmil))

print(X_train.shape)
print(X_train)
print(y_train.shape)
print(y_train)