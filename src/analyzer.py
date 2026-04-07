import pandas as pd
import os
from datetime import datetime

def es_duplicado(url, ruta="data/output/historial_engagement.xlsx"):
    if not os.path.exists(ruta):
        return False # Si no hay archivo, no hay duplicados
    
    df = pd.read_excel(ruta)
    
    # Obtenemos la fecha de hoy en el mismo formato que guardamos
    hoy = datetime.now().strftime("%Y-%m-%d")
    
    # Verificamos si existe una fila con la misma URL Y que empiece con la fecha de hoy
    # Usamos .str.contains para la fecha porque el historial guarda hora también
    duplicados = df[(df['url'] == url) & (df['fecha_analisis'].str.contains(hoy))]
    
    return not duplicados.empty

import pandas as pd
import os
from datetime import datetime

# --- FASE 4: Guardar Datos [cite: 31-33] ---
def guardar_datos(lista_metricas, ruta="data/output/", nombre_archivo="historial_engagement.xlsx"):
    """
    Toma la lista de métricas y la guarda en un Excel, 
    manteniendo un historial de las consultas anteriores. [cite: 32-33]
    """
    os.makedirs(ruta, exist_ok=True)
    ruta_completa = os.path.join(ruta, nombre_archivo) # Ahora sí está definido
    
    df_nuevo = pd.DataFrame(lista_metricas) 
    df_nuevo['fecha_analisis'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if os.path.exists(ruta_completa):
        # Si ya existe, cargamos lo viejo y pegamos lo nuevo abajo [cite: 39]
        df_previo = pd.read_excel(ruta_completa)
        df_final = pd.concat([df_previo, df_nuevo], ignore_index=True)
    else:
        df_final = df_nuevo
        
    df_final.to_excel(ruta_completa, index=False)
    return df_final

# --- FASE 5: Calcular Engagement [cite: 44-46] ---
def calcular_engagement(df):
    """
    Aplica la fórmula de probabilidad de éxito sobre el DataFrame. [cite: 45]
    """
    # Evitamos filas con 0 visualizaciones para que no explote la división
    df = df[df['visualizaciones'] > 0].copy()
    
    # Aplicamos la fórmula matemática [cite: 51]
    df['Probabilidad_Exito'] = (
        (df['likes'] + df['reposteos']) / df['visualizaciones'] * 100
    ).round(2)
    
    return df

# --- FASE 6: Mostrar Resultados [cite: 52-55] ---
def mostrar_resultados(df):
    """
    Ordena por éxito y muestra el ranking final. [cite: 54-55]
    """
    ranked = df.sort_values('Probabilidad_Exito', ascending=False)
    print("\n--- 🏆 RANKING DE ÉXITO ---")
    print(ranked.to_string(index=False))
    
    # Guardamos también una copia del ranking ordenado [cite: 62]
    ranked.to_excel('data/output/ranking_final.xlsx', index=False)
    return ranked