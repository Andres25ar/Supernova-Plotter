# Supernova-Plotter
Supernova Plotter es una herramienta desarrollada en colaboración con la estudiantes del Departamento de Física de la Facultad de Ciencias Exactas, Debora Calderon. Su objetivo principal es graficar el haz de luz generado por las supernovas, utilizando datos extraídos directamente de la página [VizieR](https://vizier.cds.unistra.fr/).

# Descripción del Proyecto

## El programa permite:

  ·Extraer datos astronómicos relacionados con supernovas desde el catálogo de datos de VizieR.
  
  ·Procesar y filtrar los datos relevantes para obtener información del brillo y comportamiento de las supernovas.
  
  ·Generar gráficos visuales que representan el haz de luz producido por las supernovas en función de sus propiedades específicas.
  
  ·El programa está diseñado para ser utilizado por estudiantes, investigadores y cualquier persona interesada en el análisis de datos astronómicos.

# Características Principales
  
**Extracción de Datos:**

Los datos se descargan directamente desde el portal de VizieR.

Soporte para múltiples conjuntos de datos astronómicos.
  
**Procesamiento de Datos:**

Filtrado de información irrelevante.

Análisis de patrones en los datos.

Conversión de datos en un formato adecuado para la visualización gráfica.

**Visualización Gráfica:**


Representación clara del haz de luz de las supernovas.

Presentacion gráficos en formatos estándar para su uso en presentaciones o publicaciones.

# Cómo Agregar Datos al Archivo combined_supernovae_data.tsv

Para agregar nuevos datos al archivo combined_supernovae_data.tsv, sigue estos pasos:

1. Descarga de Datos:

  · Ve a la página [VizieR](https://vizier.cds.unistra.fr/).

  · Busca el catalogo de supernova que deseas descargar.
  
  · Filtra los datos seleccionando las siguientes columnas:
  
      SN o Name (nombre de la supernova).
      Magnitud.
      Tiempo (ya sea JD o MJD).
      Filtro.
  
 · Descarga los datos en formato XML + CSV.
  
2. Preparación del Archivo:

  · Abre el archivo descargado en un editor de texto.
  
  · Elimina las primeras 24 líneas del archivo descargado, ya que contienen información adicional que no es relevante para el procesamiento    del programa.

  · Tambien elimina las ultimas 11 lineas, las cuales tampoco son utiles para el programa
  
3. Integración de Datos:


  · Copia los datos procesados al archivo *combined_supernovae_data.tsv*.

  · Asegúrate de mantener el formato y la estructura del archivo.

4. Verificación:

  · Verifica que los datos añadidos sean consistentes con el formato existente.

  ·Guarda los cambios y vuelve a ejecutar el programa para confirmar que los nuevos datos se procesen correctamente.

# Requisitos del Sistema

  · Lenguaje Principal: 

  *Python*

  · Dependencias:

  *Matplotlib, Pandas, NumPy, etc.*

  · Conexión a Internet para la descarga de datos desde VizieR.

# Cómo Usar el Programa

## Instalación:

  · Clona este repositorio:

    bash
    git clone https://github.com/Andres25ar/Supernova-Plotter.git
    cd Supernova-Plotter

  · Instala las dependencias necesarias (si corresponde).

## Ejecución:

  · Ejecuta el archivo principal del programa:

    bash
    python grafic_data.py
  
  · Sigue las instrucciones en pantalla para elegir las supernovas o filtros y los parámetros de análisis.

## Resultados:

  · Los gráficos generados se visualizan por pantalla mediante una GUI.

# Contribuciones

  · Este proyecto está abierto a contribuciones. Si deseas participar, por favor:

  · Haz un fork del repositorio.

  · Crea una nueva rama para tu contribución.

  · Realiza un pull request con tus cambios.

# Posibles mejoras
  
  1. Borrar los archivos .tsv de la carpeta *SupernovaeData* luego de haber sido añadidos al archivo *combined_supernovae_data.tsv* de manera automatica.

  2. Mejorar la interfaz grafica de usuario permitiendo a los usuarios elegir si mostrar los datos por supernovas o por filtros.

  3. Cambiar el nombre del archivo *grafic_data.py* a *graphic_data.py* 😅.

  4. Implementar una base de datos para guardar los datos a analizar, en lugar de los archivos .tsv.
