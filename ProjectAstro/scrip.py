import os
import pandas as pd

# Ruta de la carpeta que contiene los archivos TSV
input_folder = "E:\\AstroPythonForDebo\\ProjectAstro\\SupernovaeData"
output_file = "combined_supernovae_data.tsv"

# Diccionario para mapear nombres de columnas equivalentes
column_mapping = {
    "SN": "Name",
    "Name": "Name",
    "JD": "MJD",
    "mjd": "MJD",
    "Filt": "Filter",
    "mag": "Mag"
}

# Lista para almacenar los DataFrames de cada archivo
dataframes = []

print("Leyendo archivos TSV...")

# Iterar sobre todos los archivos en la carpeta
for filename in os.listdir(input_folder):
    if filename.endswith(".tsv"):
        file_path = os.path.join(input_folder, filename)
        try:
            # Leer el archivo TSV con el separador correcto
            df = pd.read_csv(file_path, sep=";")
            
            # Renombrar columnas según el mapeo
            df.rename(columns=column_mapping, inplace=True)
            
            # Verificar si la columna "MJD" necesita ser calculada desde "JD"
            if "JD" in df.columns:
                df["MJD"] = df["JD"] - 2400000.5
                df.drop(columns=["JD"], inplace=True)
            
            # Filtrar solo las columnas relevantes
            df = df[["Name", "MJD", "Filter", "Mag"]]
            
            # Agregar el DataFrame a la lista
            dataframes.append(df)
        except Exception as e:
            print(f"Error al procesar el archivo {filename}: {e}")

# Combinar todos los DataFrames en uno solo
combined_df = pd.concat(dataframes, ignore_index=True)

# Guardar el DataFrame combinado en un archivo TSV con punto y coma como separador
combined_df.to_csv(output_file, sep=";", index=False)

print(f"Datos combinados guardados en {output_file}")