import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Leer correctamente con separador ;
archivo = "combined_supernovae_data.tsv"
try:
    df = pd.read_csv(archivo, sep=";", names=['Name', 'MJD', 'Filter', 'Mag'], skiprows=1)
except FileNotFoundError:
    print(f"ERROR: No se encontró el archivo '{archivo}'. Verificá el nombre y la ruta.")
    exit()

# Asegurar tipos numéricos
df["MJD"] = pd.to_numeric(df["MJD"], errors='coerce')
df["Filter"] = pd.to_numeric(df["Filter"], errors='coerce')
df["Mag"] = pd.to_numeric(df["Mag"], errors='coerce')

# Eliminar filas con datos faltantes
df.dropna(subset=["Name", "MJD", "Filter", "Mag"], inplace=True)

# Convertir filtros a string por si acaso
df["Filter"] = df["Filter"].astype(str)

# Detectar filtros únicos y asignar colores
filtros_unicos = df["Filter"].unique()
colores = plt.cm.get_cmap('tab10', len(filtros_unicos))
colores_asignados = {filtro: colores(i) for i, filtro in enumerate(filtros_unicos)}

# Filtrar supernovas
supernovas = df["Name"].unique()
supernovas_aceptadas = []

for sn in supernovas:
    df_sn = df[df["Name"] == sn]
    if len(df_sn) < 6:
        continue
    tiempos = sorted(df_sn["MJD"])
    rango = tiempos[-1] - tiempos[0]
    if rango < 5:
        supernovas_aceptadas.append(sn)
        continue
    if np.max(np.diff(tiempos)) > 0.5 * rango:
        continue
    supernovas_aceptadas.append(sn)

print(f"Se encontraron {len(supernovas_aceptadas)} supernovas con curvas de luz adecuadas:")
print(supernovas_aceptadas)

# Graficar
for sn in supernovas_aceptadas:
    df_sn = df[df["Name"] == sn]
    
    plt.figure(figsize=(10, 6))
    plt.title(f'Curva de luz - Supernova {sn}')
    
    for filtro in filtros_unicos:
        df_filtro = df_sn[df_sn["Filter"] == filtro].sort_values("MJD")
        if not df_filtro.empty:
            plt.plot(df_filtro["MJD"], df_filtro["Mag"], 'o',
                    label=filtro, color=colores_asignados[filtro], alpha=0.7)
    
    plt.gca().invert_yaxis()
    plt.xlabel('Tiempo (MJD)')
    plt.ylabel('Magnitud aparente')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()