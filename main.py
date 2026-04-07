# Importamos las piezas del motor desde la carpeta src [cite: 64]
from src.targets import definir_targets
from src.fetcher import fetch_html  # Ahora usa Selenium internamente
from src.parser import obtener_metricas # Usa los Locators que investigaste
from src.analyzer import guardar_datos, calcular_engagement, mostrar_resultados, es_duplicado

def main():
    print("--- 🚀 Iniciando Analizador de Engagement ---")
    
    # 1. Definir configuración inicial (Fase 1) [cite: 6, 65]
    config = definir_targets()
    
    # 2. Entrada manual del link
    url = input("🔗 Pegá el link de la publicación (IG, TikTok o FB): ")
    
    # --- CONTROL DE INTEGRIDAD ---
    if es_duplicado(url):
        print(f"⚠️ Aviso: Este link ya fue analizado hoy. Revisá el historial para ver los resultados.")
        # Opcional: Podés preguntar "¿Querés analizarlo de nuevo? (s/n)"
        continuar = input("¿Deseás forzar un nuevo análisis? (s/n): ")
        if continuar.lower() != 's':
            return # Cortamos la ejecución aquí
    # ------------------------------------
    
    # 3. Descarga del contenido (Fase 2) [cite: 14, 15]
    # fetch_html ahora devuelve el 'driver' de Selenium para poder extraer datos dinámicos
    driver = fetch_html(url)
    
    if driver:
        # 4. Extracción de métricas (Fase 3) [cite: 24, 25]
        metricas = obtener_metricas(driver, url)
        
        # Cerramos el navegador ni bien terminamos de sacar los datos
        driver.quit()
        
        if metricas:
            # 5. Personalización del tema (Ideal para Giros Idiomas)
            # Ej: "Clase de portugués", "Promo IA", etc.
            metricas['tema'] = input("📝 ¿De qué trata este contenido?: ")
            
            # 6. Persistencia en Historial (Fase 4) [cite: 31, 32]
            # Esta función ahora lee el Excel viejo y le pega los datos nuevos [cite: 33]
            df_historico = guardar_datos([metricas])
            
            # 7. Cálculo de Probabilidad de Éxito (Fase 5) [cite: 44, 45]
            # Se aplica sobre todo el historial acumulado [cite: 46]
            df_calculado = calcular_engagement(df_historico)
            
            # 8. Ranking y Salida Final (Fase 6) [cite: 53, 54]
            # Ordena de mayor a menor éxito para la toma de decisiones [cite: 55]
            mostrar_resultados(df_calculado)
            
        else:
            print("❌ No se pudieron extraer métricas. Revisar locadores.")
    else:
        print("❌ Error al conectar con la página.")

if __name__ == "__main__":
    main() # Punto de entrada del script