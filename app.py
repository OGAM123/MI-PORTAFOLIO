import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Mi Portafolio", page_icon="💰")

st.title("🚀 Mi Rastreador de Inversiones")
st.write("Configura tus acciones y recibe alertas visuales.")

# Lista de tus acciones (puedes cambiarlas aquí)
mis_acciones = st.multiselect("Selecciona tus acciones:", ["ALICORC1", "BACKUSI1", "AUNA", "TTD", "INRETC1", "NVDA", "KO", "BBVAC1", "ORYGENC1", "SPHQ"], default=["ALICORC1", "NVDA"])

# Configurar alerta
umbral = st.number_input("Avísame si alguna baja de ($):", value=150.0)

for ticker in mis_acciones:
    datos = yf.Ticker(ticker)
    precio = datos.fast_info['last_price']
    
    col1, col2 = st.columns([1, 3])
    with col1:
        if precio < umbral:
            st.error(f"⚠️ {ticker}: ${precio:.2f}")
        else:
            st.success(f"✅ {ticker}: ${precio:.2f}")
    with col2:
        # Gráfico pequeño de los últimos 5 días
        hist = datos.history(period="5d")
        st.line_chart(hist['Close'], height=100)
