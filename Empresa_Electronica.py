# Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y quieres
# analizar los datos de calidad de los componentes utilizados en la producción de dichos
# dispositivos. Tienes un conjunto de datos que contiene información sobre la fecha de
# producción, el tipo de componente, el lote al que pertenece el componente y la
# puntuación de calidad del componente (un número entre 0 y 100). Quieres analizar estos
# datos para determinar cuál es el tipo de componente con la puntuación de calidad más
# alta, cuántos componentes se produjeron en cada mes y cuál es la puntuación de calidad
# promedio de cada tipo de componente.

# Pista: puede ser util investigar np.unique y np.argmax

# Importacion del modulo
import numpy as np

# Crear un array con los datos
datos = np.array([
    ['2022-01-01', 'Componente 1', 'Lote A', 80],
    ['2022-01-15', 'Componente 1', 'Lote B', 90],
    ['2022-02-01', 'Componente 2', 'Lote C', 85],
    ['2022-02-15', 'Componente 2', 'Lote D', 95],
    ['2022-03-01', 'Componente 1', 'Lote E', 75],
    ['2022-03-15', 'Componente 2', 'Lote F', 90]
])

# Determinar el tipo de componente con la puntuación de calidad más alta
Puntuacion_Calidad = datos[:,3].astype(int)

Maxima_Puntuacion = np.argmax(Puntuacion_Calidad)

Componente_max = datos[Maxima_Puntuacion,1]
Puntuacion_max = Puntuacion_Calidad[Maxima_Puntuacion]

print(f"El producto de una calidad alta es el {Componente_max} con {Puntuacion_max} de calidad")
print("")

# Cuántos componentes se produjeron en cada mes
componentes, conteo = np.unique(datos[:,1], return_counts=True)

for cp, c in zip(componentes, conteo):
    print(cp, c)
print("")

# cuál es la puntuación de calidad promedio de cada tipo de componente.
media_componente = datos[:,3].astype(float)
componentes_media = datos[:,1]
componente_unico = np.unique(componentes_media)

promedio_componente = [
    media_componente[componentes_media == cu].mean()
    for cu in componente_unico
]

for cu, pc in zip(componente_unico, promedio_componente):
    print(f"Media del {cu}: {pc}")