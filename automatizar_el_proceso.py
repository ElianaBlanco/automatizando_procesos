import pandas as pd
import argparse
import requests

def procesar_dataframe(df):
    # Lógica de procesamiento del DataFrame
    # ...

    return df

def descargar_datos_y_procesar(url):
    # Realizar el GET request para obtener los datos
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        # Guardar la respuesta en un archivo CSV
        nombre_archivo_csv = 'datos_descargados.csv'
        with open(nombre_archivo_csv, 'w') as archivo_csv:
            archivo_csv.write(respuesta.text)
            print(f"Datos descargados y guardados en '{nombre_archivo_csv}'")

        # Leer los datos en un DataFrame
        df = pd.read_csv(nombre_archivo_csv)

        # Procesar el DataFrame
        df_procesado = procesar_dataframe(df)

        # Guardar el resultado como CSV procesado
        nombre_archivo_resultado = 'datos_procesados.csv'
        df_procesado.to_csv(nombre_archivo_resultado, index=False)
        print(f"Datos procesados y guardados en '{nombre_archivo_resultado}'")
    else:
        print("Error al descargar los datos")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL para descargar los datos")
    args = parser.parse_args()

    descargar_datos_y_procesar(args.url)
    
#Leer todo
#python nombre_del_script.py https://tu_url_de_los_datos.com/datos.csv
