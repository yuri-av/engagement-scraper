# Importamos las funciones desde la carpeta src
from src.targets import definir_targets
from src.fetcher import fetch_html
from src.parser import parsear_metricas
from src.analyzer import guardar_datos, calcular_engagement, mostrar_resultados

def main():
    # 1. Definir qué analizar [cite: 65]
    config = definir_targets()
    metricas = []
    
    # Podés usar tu lógica de input() aquí o recorrer la lista
    url = input("Pegá el link a analizar: ")
    
    # 2. Pipeline [cite: 65]
    html = fetch_html(url)
    m = parsear_metricas(html)
    
    if m:
        m['tema'] = "Análisis Manual" # Agregamos el tema manualmente
        metricas.append(m)
        
        df = guardar_datos(metricas)
        df = calcular_engagement(df)
        mostrar_resultados(df)

if __name__ == "__main__":
    main() 