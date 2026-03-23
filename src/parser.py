"""parsear_metricas() recibe dos cosas — el HTML crudo que descargó fetch_html() y el tema al que corresponde ese post — 
y su trabajo es buscar adentro de ese HTML los números que nos interesan: likes, resposteos y visualizaciones.
Pensalo así. Cuando vos abrís Instagram en el navegador y ves que un post tiene 450 likes, 
ese número está escrito en algún lugar del código HTML de la página. BeautifulSoup lo que hace
es leer todo ese HTML y permitirte decirle "buscame el tag donde está el número de likes" para extraerlo.

El flujo completo sería:
===============================================================================
fetch_html()         →    parsear_metricas()     →    guardar_datos()
descarga el HTML          encuentra los números        los guarda en Excel
===============================================================================
El problema concreto que tenemos ahora es que Instagram no pone los números directamente en el HTML — 
los carga después con JavaScript, entonces cuando fetch_html() descarga la página, los likes todavía no aparecen. 
Por eso la función por ahora devuelve ceros — es un esqueleto que vamos a completar cuando integremos Selenium, 
que sí puede esperar a que JavaScript cargue todo."""

from bs4 import BeautifulSoup

def parsear_metricas(html, tema):
    if html is None:
        return None
    soup = BeautifulSoup(html, "html.parser")
    
    resultado = {
        "tema": tema,
        "likes": 0,
        "reposteos": 0,
        "visualizaciones": 0
    }
    
    return resultado