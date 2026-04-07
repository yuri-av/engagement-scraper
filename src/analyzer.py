import pandas as pd
from datetime import date
import os

def guardar_datos(lista_metricas, ruta="data/output/"):
    os.makedirs(ruta, exist_ok=True)
    df = pd.DataFrame(lista_metricas)
    nombre = f"{ruta}metricas_{date.today()}.xlsx"
    df.to_excel(nombre, index=False)
    return df

def calcular_engagement(df):
    # Evitamos división por cero filtrando visualizaciones > 0
    df = df[df['visualizaciones'] > 0].copy()
    df['Probabilidad_Exito'] = ((df['likes'] + df['resposteos']) / df['visualizaciones'] * 100).round(2)
    return df

def mostrar_resultados(df):
    # Orden descendente para ver el éxito primero [cite: 54, 62]
    ranked = df.sort_values('Probabilidad_Exito', ascending=False)
    print(ranked.to_string(index=False))
    ranked.to_excel('data/output/ranking_final.xlsx', index=False)
    return ranked