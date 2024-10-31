import streamlit as st
import base64
from ETFS import instrumentos_financieros, obtener_informacion_etf
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from Graficas import estadistica

# Función auxiliar para obtener datos de los instrumentos seleccionados
def obtener_datos_instrumentos(instrumentos_seleccionados):
    datos = []
    for instrumento in instrumentos_seleccionados:
        info = {
            "nombre": instrumento["nombre"],
            "descripcion": instrumento["descripcion"],
            "simbolo": instrumento["simbolo"],
            "moneda": instrumento["moneda"],
            "paga_dividendos": instrumento["paga_dividendos"]
        }
        datos.append(info)
    return datos

# Cargar el logo y la imagen de México
logo_path = "./Allianz_logo.png"  # Cambia la ruta si el logo está en otra carpeta
mexico_image_path = "./Mexico.jpeg"  # Ruta relativa de la imagen de México

# Función para convertir la imagen a base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Convertir el logo a base64
logo_base64 = get_base64_image(logo_path)

# CSS para ajustar el estilo del título
st.markdown(f"""
    <style>
        .logo-container {{
            position: absolute;
            top: 5px;
            right: 15px;
            width: 100px;
        }}
        .main-title {{
            margin-top: 70px;
            font-size: 30px;
            text-align: center;
            color: #666666;
        }}
        .justified-text {{
            text-align: justify;
            font-size: 16px;
        }}
        .section-title {{
            font-size: 24px;
            font-weight: bold;
            color: #004481;
            margin-bottom: 20px;
            margin-top: 30px;
            text-align: left;
        }}
        .instrument-title {{
            font-size: 20px;
            font-weight: bold;
            color: #5DADE2;
        }}
        .description-text {{
            text-align: justify;
            font-size: 16px;
        }}
        .justified-column-text {{
            text-align: justify;
            font-size: 16px;
            margin-bottom: 20px;
        }}
        .center-content {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}">
    </div>
""", unsafe_allow_html=True)

# Barra lateral con las opciones fijas
st.sidebar.markdown("<div class='main-menu-title'>Menu Principal</div>", unsafe_allow_html=True)
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Opciones del menú en la barra lateral (sin "Graficas" y "Portafolio de Inversión")
option = st.sidebar.radio("Selecciona una opción:", ["Inicio", "Resumen", "Estadística"], key="menu_option")

# Mostrar contenido según la opción seleccionada
if option == "Inicio":
    st.markdown("<h1 class='main-title'>Simulador OptiMaxx Patrimonial</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="section-title">¿Quiénes somos?</div>
    <div class="justified-text">
    Allianz es la aseguradora Alemana líder en el mercado con presencia internacional, atendiendo más de 125 millones de clientes, en casi 70 países. Gracias al esfuerzo de todos, desde 1890 seguimos trabajando para entregarle tranquilidad a cada uno de los clientes que ponen su confianza en nosotros.<br><br>
    En Allianz México seguimos comprometidos con asegurar el futuro de cada mexicano, ofreciéndole soluciones que se ajusten a todas sus necesidades. Tenemos alrededor de 500 empleados distribuidos en 4 oficinas regionales: Centro, Norte, Occidente & Bajío y Sureste.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>¿Por qué elegir Allianz?</div>", unsafe_allow_html=True)

    # Sección de tres columnas para "¿Por qué elegir Allianz?"
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='center-content'>", unsafe_allow_html=True)
        st.image("https://img.icons8.com/ios-filled/50/4682B4/handshake.png")
        st.markdown("<div class='justified-column-text'>130 años asegurando lo que más te importa en el mundo.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='center-content'>", unsafe_allow_html=True)
        st.image("https://img.icons8.com/ios-filled/50/4682B4/gender-neutral-user.png")
        st.markdown("<div class='justified-column-text'>En México, más de 250 mil clientes han depositado su confianza con nosotros, recibiendo asesoría directa por parte de nuestros más de 3 mil distribuidores.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='center-content'>", unsafe_allow_html=True)
        st.image("https://img.icons8.com/ios-filled/50/4682B4/combo-chart.png")
        st.markdown("<div class='justified-column-text'>157 mil empleados atienden aproximadamente 125 millones de clientes en más de 70 países.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Imagen de México
    st.markdown("<br>", unsafe_allow_html=True)
    _, centered_image, _ = st.columns([1, 2, 1])
    with centered_image:
        st.image(mexico_image_path, width=350)

elif option == "Resumen":
    st.markdown("<h1 class='main-title'>Instrumentos Financieros</h1>", unsafe_allow_html=True)
    st.markdown("<p>Seleccione uno o más instrumentos financieros de su interés:</p>", unsafe_allow_html=True)
    
    seleccionados = st.multiselect("Instrumentos Financieros", options=[inst['nombre'] for inst in instrumentos_financieros])

    # Botón para mostrar detalles
    if st.button("Mostrar Detalles"):
        st.markdown("<h2 class='section-title'>Detalles de los Instrumentos Financieros</h2>", unsafe_allow_html=True)
        
        # Guardar la selección de ETFs en la sesión
        st.session_state["seleccionados"] = [inst["simbolo"] for inst in instrumentos_financieros if inst["nombre"] in seleccionados]
        
        # Obtener datos de los instrumentos seleccionados
        instrumentos_a_mostrar = [inst for inst in instrumentos_financieros if inst['nombre'] in seleccionados]
        datos_instrumentos = obtener_datos_instrumentos(instrumentos_a_mostrar)

        # Mostrar detalles de cada instrumento seleccionado
        for dato in datos_instrumentos:
            st.markdown(f"<div class='instrument-title'>Instrumento: {dato['nombre']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='description-text'>{dato['descripcion']}</div>", unsafe_allow_html=True)
            st.write(f"**Símbolo:** {dato['simbolo']}")
            st.write(f"**Moneda:** {dato['moneda']}")
            st.write(f"**Paga Dividendos:** {dato['paga_dividendos']}")
            st.write("---")

elif option == "Estadística":
    # Título "Portafolio de Inversión" en la sección Estadística con el mismo formato de "Instrumentos Financieros"
    st.markdown("<h1 class='main-title'>Portafolio de Inversión</h1>", unsafe_allow_html=True)
    
    # Aquí puedes agregar más contenido específico para la sección de Estadística
    # ...

# Llamada a la función estadística desde el archivo Graficas
if option == "Estadística":
    estadistica()
