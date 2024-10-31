import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Calculo import calcular_rendimiento_riesgo, calcular_retorno_esperado

# Configuración de estilo minimalista para seaborn
sns.set(style="whitegrid")

# Configuración de tamaños de fuente en matplotlib
plt.rcParams.update({
    "axes.facecolor": "white",
    "axes.edgecolor": "#E5E5E5",
    "grid.color": "#E5E5E5",
    "axes.labelcolor": "#333333",
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "font.size": 8,
    "axes.titlesize": 10,
    "axes.labelsize": 8,
    "legend.fontsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7
})

# Función para validar y ajustar los pesos de los instrumentos seleccionados
def asignar_pesos():
    seleccionados = st.session_state.get("seleccionados", [])
    if len(seleccionados) == 0:
        st.sidebar.warning("No se han seleccionado instrumentos financieros en la sección de Resumen.")
        return

    # Título de Asignación de Pesos
    st.sidebar.markdown("<h2 class='section-title'>Asignación de Pesos</h2>", unsafe_allow_html=True)

    # Entrada de pesos de inversión
    pesos = {}
    total_peso = 0
    if len(seleccionados) == 1:
        st.sidebar.write(f"Asignación automática: 100% en {seleccionados[0]}")
        pesos[seleccionados[0]] = 100
    else:
        for instrumento in seleccionados:
            pesos[instrumento] = st.sidebar.number_input(
                f"Porcentaje de inversión para {instrumento}", min_value=0, max_value=100, value=0, step=1
            )
            total_peso += pesos[instrumento]

        if total_peso != 100:
            st.sidebar.error("La suma de los porcentajes debe ser exactamente 100%. Ajuste los valores.")
        else:
            st.sidebar.success("Asignación de pesos completada con éxito.")

    # Título de Capital
    st.sidebar.markdown("<h2 class='section-title'>Capital</h2>", unsafe_allow_html=True)

    # Entrada de capital a invertir con un mínimo de $500,000
    capital_invertir = st.sidebar.number_input(
        "Ingrese la cantidad a invertir", min_value=500000, value=500000, step=10000, format="%d"
    )

    st.sidebar.markdown("<h2 class='section-title'>Periodo</h2>", unsafe_allow_html=True)
    periodos = {
        "1 mes": "1mo",
        "3 meses": "3mo",
        "6 meses": "6mo",
        "1 año": "1y",
        "YTD": "ytd",
        "3 años": "3y",
        "5 años": "5y",
        "10 años": "10y"
    }
    periodo_seleccionado_nombre = st.sidebar.selectbox("Seleccione el periodo de inversión", list(periodos.keys()))
    periodo_seleccionado = periodos[periodo_seleccionado_nombre]

    if st.sidebar.button("Calcular"):
        st.sidebar.success("Cálculo realizado exitosamente con los parámetros seleccionados.")
        st.session_state["mostrar_resultados"] = True
        st.session_state["periodo_seleccionado"] = periodo_seleccionado
        st.session_state["capital_invertir"] = capital_invertir  # Guardar capital en session state

# Código principal para la sección de Estadística
def estadistica():
    st.markdown("<h2 class='section-title'>Rendimiento y Riesgo</h2>", unsafe_allow_html=True)
    asignar_pesos()

    if st.session_state.get("mostrar_resultados", False):
        seleccionados = st.session_state.get("seleccionados", [])
        periodo = st.session_state.get("periodo_seleccionado", None)
        capital = st.session_state.get("capital_invertir", None)

        if seleccionados and periodo:
            periodos_fijos = ["1mo", "3mo", "6mo", "1y", "ytd", "3y", "5y", "10y"]
            resultados = calcular_rendimiento_riesgo(seleccionados, periodos_fijos)

            # Convertir resultados a DataFrame y mostrar tabla
            data = []
            for resultado in resultados:
                for etf, valores in resultado.items():
                    fila = {"ETF": etf}
                    for periodo_key, metrics in valores.items():
                        fila[f"Rendimiento {periodo_key.upper()}"] = metrics.get("rendimiento")
                        fila[f"Riesgo {periodo_key.upper()}"] = metrics.get("riesgo")
                    data.append(fila)

            resultados_df = pd.DataFrame(data)

            if not resultados_df.empty:
                resultados_df_display = resultados_df.copy()
                for col in resultados_df_display.columns[1:]:
                    resultados_df_display[col] = resultados_df_display[col].apply(lambda x: f"{x:.2f}%" if pd.notnull(x) else "-")
                st.table(resultados_df_display)

            # Checkbox para mostrar gráficas adicionales y opciones
            mostrar_opciones = st.checkbox("Ver más opciones")

            # Espacio dinámico para el subtítulo "Retornos esperados" y la tabla
            subtitulo_y_tabla_espacio = st.empty()

            # Mostrar "Retornos esperados" y su tabla solo si el checkbox NO está activado
            if not mostrar_opciones:
                with subtitulo_y_tabla_espacio:
                    st.markdown("<h2 class='section-title'>Retornos esperados</h2>", unsafe_allow_html=True)
                    retorno_esperado = calcular_retorno_esperado(resultados, capital)
                    retorno_esperado_df = pd.DataFrame(retorno_esperado)
                    retorno_esperado_df["Retorno Esperado (%)"] = retorno_esperado_df["Retorno Esperado (%)"].apply(lambda x: f"{x:.2f}%")
                    retorno_esperado_df["Retorno Esperado (Capital)"] = retorno_esperado_df["Retorno Esperado (Capital)"].apply(lambda x: f"${x:,.2f}")
                    st.table(retorno_esperado_df)

            # Si el checkbox está activado, mostrar las gráficas pero NO el subtítulo ni la tabla de "Retornos esperados"
            if mostrar_opciones:
                st.write(resultados_df_display)

                # Convertir la tabla a formato largo para gráficos
                resultados_long_df = resultados_df.melt(id_vars="ETF", var_name="Métrica", value_name="Valor")
                
                # Gráfica de líneas para rendimiento y riesgo
                rendimiento_df = resultados_long_df[resultados_long_df["Métrica"].str.contains("Rendimiento")]
                riesgo_df = resultados_long_df[resultados_long_df["Métrica"].str.contains("Riesgo")]

                # Gráfico de rendimiento
                plt.figure(figsize=(6, 3))
                sns.lineplot(data=rendimiento_df, x="Métrica", y="Valor", hue="ETF", marker="o", palette="Blues_r")
                plt.title("Evolución del Rendimiento por Periodo")
                plt.xlabel("Periodo")
                plt.ylabel("Rendimiento (%)")
                plt.xticks(rotation=45)
                plt.legend(title="ETF", loc="upper left")
                plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.2f}%"))
                st.pyplot(plt)

                # Gráfico de riesgo
                plt.figure(figsize=(6, 3))
                sns.lineplot(data=riesgo_df, x="Métrica", y="Valor", hue="ETF", marker="o", palette="Reds_r")
                plt.title("Evolución del Riesgo por Periodo")
                plt.xlabel("Periodo")
                plt.ylabel("Riesgo (%)")
                plt.xticks(rotation=45)
                plt.legend(title="ETF", loc="upper left")
                plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.2f}%"))
                st.pyplot(plt)
