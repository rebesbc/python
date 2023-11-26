import numpy as np
import matplotlib.pyplot as plt

# Datos de 10 personas -> [edad, ahorro]
personas = np.array([[0.3, 0.4], [0.4, 0.3],
                     [0.3, 0.2], [0.4, 0.1],
                     [0.5, 0.2], [0.4, 0.8],
                     [0.6, 0.8], [0.5, 0.6],
                     [0.7, 0.6], [0.8, 0.5]
                    ]
                   )

# 1: persona con tarjeta platinum aprobada
# 0: persona con tarjeta platinum denegada
clases = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# Gráfica de dispersión
plt.figure(figsize=(7, 7))
plt.title("¿Tarjeta Platinum?", fontsize=20)
plt.scatter(personas[clases == 0].T[0],
            personas[clases == 0].T[1],
            marker="x", s=180, color="red",
            linewidth=5, label="Denegada")
plt.scatter(personas[clases == 1].T[0],
            personas[clases == 1].T[1],
            marker="o", s=180, color="blue",
            linewidth=5, label="Aprobada")
plt.xlabel("Edad", fontsize=15)
plt.ylabel("Ahorro", fontsize=15)
plt.legend(bbox_to_anchor=(1.3, 0.15))
plt.box(False)
plt.xlim((0, 1.01))
plt.ylim((0, 1.01))
plt.grid()
plt.show()

# Peso_1*x_1 + Peso_2*x_2 + ... + Peso_n*x_n
# Umbral = Bias, B
def activacion(pesos, x, umbral):
    z = pesos * x
    if z.sum() + umbral > 0:
        return 1
    else:
        return 0
    
# Entrenamiento del perceptrón
pesos = np.random.uniform(-1, 1, size=2)
umbral = np.random.uniform(-1, 1)
tasa_de_aprendizaje = 0.01
epocas = 100

for epoca in range(epocas):
    error_total = 0
    # Controlar por el número de personas que tenemos en el DataSet
    for i in range(len(personas)):
        # Sólo la primera iteración tiene valores arbitrarios en el cálculo
        prediccion = activacion(pesos, personas[i], umbral)
        error = clases[i] - prediccion

        # Elevar al cuadrado para
        # - Dar mayor peso a los errores grandes
        # - Dar menor peso a los errores pequeños
        # - Evitar números negativos
        error_total += error**2

        # Peso para la primera entrada de la persona [edad]
        pesos[0] += tasa_de_aprendizaje * personas[i][0] * error
        # Peso para la segunda entrada de la persona [ahorro]
        pesos[1] += tasa_de_aprendizaje * personas[i][1] * error
        umbral += tasa_de_aprendizaje * error
    print(str(error_total), end="... ")

# Ejemplos
# Persona de 10 años y tiene 0 pesos
activacion1 = activacion(pesos, [0.1, 0], umbral)
print("\n\nPersona 1 [10, $0.00] = " + str(activacion1))
# Persona de 50 años y tiene $80,000 pesos
activacion2 = activacion(pesos, [0.5, 0.8], umbral)
print("Persona 2 [50, $80,000.00] = " + str(activacion2))
# Persona de 50 años y tiene $50,000 pesos
activacion3 = activacion(pesos, [0.5, 0.5], umbral)
print("Persona 3 [50, $50,000.00] = " + str(activacion3))

# Graficar línea
plt.figure(figsize=(6, 5), dpi=200)
plt.title("¿Tarjeta Platinum?", fontsize=20)

plt.scatter(personas[clases == 0].T[0], 
            personas[clases == 0].T[1], 
            marker="x", s=180, color="red",
            linewidths=5, label="Denegada")

plt.scatter(personas[clases == 1].T[0],
            personas[clases == 1].T[1], 
            marker="o", s=180, color="blue",
            linewidths=5, label="Aprobada")

for edad in np.arange(0, 1, 0.05):
    for ahorro in np.arange(0, 1, 0.05):
        color = activacion(pesos, [edad, ahorro], umbral)
        if color == 1:
            plt.scatter(edad, ahorro, marker="s", s=110,
                        color="blue", alpha=0.2, linewidths=0)
        else:
            plt.scatter(edad, ahorro, marker="s", s=110, 
                        color="red", alpha=0.2, linewidths=0)
            
plt.xlabel("Edad", fontsize=15)
plt.ylabel("Ahorro", fontsize=15)
plt.legend(bbox_to_anchor=(1.3, 0.15))
plt.box(False)
plt.xlim((0, 1.01))
plt.ylim((0, 1.01))
plt.show()