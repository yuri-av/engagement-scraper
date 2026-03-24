import pandas as pd
from datetime import date
import os

# Crea un archivo excel y lo guarda en el disco // Formato de fecha: AAAA/MM/DD


lista_metricas = [ # TEST: BORRAR ANTES DE USAR EN PRODUCCION
    {"tema": "branding", 
     "likes": 150, 
     "resposteos": 20, 
     "visualizaciones": 1000},
    
    {"tema": "IA en marketing", 
     "likes": 450, 
     "resposteos": 85, 
     "visualizaciones": 5000},
]

# Dirección del archivo  (PERSONALIZAR SI NECESARIO EN MAIN)

def guardar_datos(lista_metricas,ruta = "data/output/"):
    
    # Crea carpeta si no existe en la máquina
    os.makedirs(ruta, exist_ok = True)
    nombre_archivo  =  "metricas_"    
    # Crea el DataFrame
    df = pd.DataFrame(lista_metricas)
    hoy = date.today()
    # Crea archivo en la carpeta 
    excel = df.to_excel(f"{ruta}{nombre_archivo}{hoy}.xlsx", index=False)

    return df
    
guardar_datos(lista_metricas)