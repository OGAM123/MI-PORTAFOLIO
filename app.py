import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Mi Portafolio", page_icon="💰")

st.title("🚀 Mi Rastreador de Inversiones")

# 1. LISTA DE ACCIONES (Aquí puedes añadir las que quieras)
# Importante: Para acciones de Perú, usa .LM al final
tickers_disponibles = ["BACKUSI1.LM", "NVDA", "ALICORC1.LM", "TTD", "INRETC1.LM", "BBVAC1.LM", "ORYGENC1.LM", "SPHQ", "AUNA.LM", "KO", "AAPL"]

# 2. SELECCIÓN DE USUARIO
seleccion = st.multiselect("Selecciona tus acciones:", tickers_disponibles, default=["AAPL"])

# 3. CONFIGURAR ALERTA
umbral = st.number_input("Avísame si baja de ($):", value=10.0)

# 4. PROCESAR CADA ACCIÓN
for ticker in seleccion:
    try:
        stock = yf.Ticker(ticker)
        # Obtenemos el precio actual de forma segura
        precio = stock.fast_info['last_price']
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            if precio < umbral:
                st.error(f"⚠️ {ticker}: ${precio:.2f}")
            else:
                st.success(f"✅ {ticker}: ${precio:.2f}")
        
        with col2:
            # Gráfico de los últimos 5 días
            hist = stock.history(period="5d")
            if not hist.empty:
                st.line_chart(hist['Close'], height=100)
                
    except Exception:
        st.warning(f"No se pudo cargar {ticker}. Revisa si el nombre es correcto.")
