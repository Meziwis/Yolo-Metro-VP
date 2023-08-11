# Extracción de Marcos de Video basado en YAML

Este script de Python se utiliza para extraer marcos de un video en intervalos de tiempo especificados en un archivo YAML.

## Requisitos

- Python 3.x
- Bibliotecas Python: av, os, yaml

## Uso

1. Asegúrate de tener un archivo YAML (`input.yaml`) con la siguiente estructura:

```yaml
input_paths:
  - Videos/cam_6_hospital_2/cam_6_hosp_2.avi
output_paths:
  - output
fps:
  - 10
start_times:
  - [00:00:01, 00:00:11]
end_times:
  - [00:00:05, 00:00:15]
```
1. Ejecuta el script extract_frames.py proporcionando el archivo YAML como entrada:
    
    ```bash
    python extract_frames.py
    ```
2. Los marcos extraídos se guardarán en directorios de salida correspondientes a cada video en la carpeta output.

## Detalles del Script

El script `extract_frames.py` realiza las siguientes acciones:

- Abre el archivo de video de entrada.
- Analiza los tiempos de inicio y finalización especificados en el archivo YAML.
- Calcula los números de cuadro correspondientes a esos tiempos.
- Crea directorios de salida para cada video en la carpeta de salida.
- Extrae y guarda marcos del video en intervalos especificados.

## Ajustes

Si deseas ajustar los parámetros, como la carpeta de salida o el formato de salida de los marcos, puedes hacerlo directamente en el script. Por ejemplo:

- Para cambiar la carpeta de salida, modifica la variable `output_path`.
- Para cambiar el formato de los marcos de salida, ajusta el nombre de archivo en la línea que define `output_filename`.

## Notas

- Asegúrate de tener los videos de entrada en las rutas especificadas en el archivo YAML.
- Los tiempos deben estar en formato HH:MM:SS.

Si tienes alguna pregunta o necesitas más información sobre cómo usar o ajustar el script, consulta el código fuente y los comentarios en `extract_frames.py`.

**¡Disfruta extrayendo marcos de tus videos de manera eficiente con este script!**
