import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo (reemplaza estos datos con tus propios datos)
Xi = np.array([0, 1, 2, 3, 4, 5])
Yi = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])

# Grado del polinomio (por ejemplo, polinomio de grado 2 para una parábola)
grado = 2

# Ajusta el polinomio a los datos
coeficientes = np.polyfit(Xi, Yi, grado)

# Crea una función polinómica a partir de los coeficientes
polinomio = np.poly1d(coeficientes)

# Valores x para el gráfico
x_valores = np.linspace(Xi.min(), Xi.max(), 100)

# Calcula los valores de y correspondientes al polinomio
y_valores = polinomio(x_valores)

# Imprime el polinomio resultante
print("Polinomio de regresión:", polinomio)

# Gráfico de los datos y el polinomio ajustado
plt.scatter(Xi, Yi, label="Datos")
plt.plot(x_valores, y_valores, label="Regresión Polinómica", color='red')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
