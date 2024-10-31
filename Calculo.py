import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Función para calcular rendimiento y riesgo de los ETFs en diferentes periodos
def calcular_rendimiento_riesgo(etf_symbols, periodos=["1mo", "3mo", "6mo", "1y", "ytd", "3y", "5y", "10y"]):
    resultados = []

    for etf in etf_symbols:
        data_periodos = {}
        for periodo in periodos:
            # Ajuste especial para 3 años usando fechas específicas
            if periodo == "3y":
                end_date = datetime.now()
                start_date = end_date - timedelta(days=3*365)  # Aproximadamente 3 años
                data = yf.Ticker(etf).history(start=start_date, end=end_date)
            else:
                # Para otros periodos, usar el parámetro `period`
                data = yf.Ticker(etf).history(period=periodo)

            if data.empty:
                print(f"No hay datos para {etf} en el periodo {periodo}")
                data_periodos[periodo] = {"rendimiento": None, "riesgo": None}
                continue
            
            # Cálculo del rendimiento total
            precio_inicial = data['Close'].iloc[0]
            precio_final = data['Close'].iloc[-1]
            rendimiento = ((precio_final / precio_inicial) - 1) * 100

            # Cálculo de riesgo (volatilidad anualizada)
            retornos_diarios = data['Close'].pct_change().dropna()
            riesgo = retornos_diarios.std() * (252 ** 0.5) * 100

            # Guardar resultados para el periodo
            data_periodos[periodo] = {"rendimiento": round(rendimiento, 2), "riesgo": round(riesgo, 2)}

        # Agregar los resultados de este ETF a la lista de resultados
        resultados.append({etf: data_periodos})

    return resultados

# Calculo.py

def calcular_retorno_esperado(rendimientos_riesgos, capital_invertir):
    """
    Calcula el retorno esperado en porcentaje y en capital para cada ETF en función del capital invertido.

    Parámetros:
    - rendimientos_riesgos (list): Lista de diccionarios con los rendimientos de cada ETF.
    - capital_invertir (float): Capital total invertido en los ETFs.

    Retorna:
    - list: Lista de diccionarios con el retorno esperado en porcentaje y en capital para cada ETF.
    """
    resultados_retorno = []

    for rendimiento in rendimientos_riesgos:
        for etf, valores in rendimiento.items():
            # Calcular el retorno promedio basado en los periodos
            retorno_promedio = sum([valores[periodo]["rendimiento"] for periodo in valores]) / len(valores)
            retorno_porcentaje = retorno_promedio
            retorno_capital = capital_invertir * (retorno_porcentaje / 100)  # Capital en términos de retorno esperado
            
            resultados_retorno.append({
                "ETF": etf,
                "Retorno Esperado (%)": retorno_porcentaje,
                "Retorno Esperado (Capital)": retorno_capital
            })
    
    return resultados_retorno
