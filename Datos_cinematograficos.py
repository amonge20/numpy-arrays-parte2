# Supongamos que tienes un conjunto de datos de películas que contiene información
# sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar
# estos datos para determinar cuál es el género de película más popular, cuántas películas
# se lanzaron en cada década y cuál es la duración promedio de cada género de película.

# importamos los siguientes modulos
import numpy as np

# -----------------------------
# DATOS CINEMATOGRÁFICOS
# -----------------------------
peliculas = np.array([
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Acción', 110, 2005, 7.8],
    ['Peli 3', 'Drama', 95, 2010, 6.9],
    ['Peli 4', 'Comedia', 100, 1985, 7.5],
    ['Peli 5', 'Acción', 130, 2015, 8.1],
    ['Peli 6', 'Drama', 115, 2000, 7.7],
    ['Peli 7', 'Comedia', 90, 1995, 8.2],
    ['Peli 8', 'Acción', 105, 2010, 7.4],
    ['Peli 9', 'Drama', 125, 1980, 6.8],
    ['Peli 10', 'Comedia', 95, 2000, 8.0]
], dtype=object)

# -------------------------------
# Género de película más popular
# -------------------------------
generos = peliculas[:,1]
genero_unico = np.unique(generos)

conteo = np.array([np.count_nonzero(generos == g) for g in genero_unico])
indice_popular = np.argmax(conteo)
genero_popular = genero_unico[indice_popular]

print("Género más popular:", genero_popular)
print("")

# ----------------------------------
# Cantidad de películas por década
# ----------------------------------
años = peliculas[:,3].astype(int)
decadas = (años // 10) * 10

decadas_unicas, conteo_decada = np.unique(decadas, return_counts=True)
for d, c in zip(decadas_unicas, conteo_decada):
    print(f"{d}s: {c} películas")
print("")

# ----------------------------------
# Duración promedio por género
# ----------------------------------
duraciones = peliculas[:,2].astype(float)

promedio_duracion = [
    duraciones[generos == g].mean()
    for g in genero_unico
]

for g, dur in zip(genero_unico, promedio_duracion):
    print(f"Duración media del género {g}: {dur:.1f}s")