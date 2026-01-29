import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Mi Portafolio Personalizado", page_icon="💰")
st.title("📈 Monitor con Objetivos Individuales")

# 1. Lista de acciones disponibles
tickers_disponibles = ["AAPL", "NVDA", "BACKUSI1.LM", "ALICORC1.LM", "TTD", "INRETC1.LM", "BBVAC1.LM", "ORYGENC1.LM", "SPHQ", "AUNA.LM", "KO"]

# 2. Selección de acciones
seleccion = st.multiselect("Selecciona tus acciones:", tickers_disponibles, default=["AAPL"])

# Diccionario para guardar los límites de cada acción
limites = {}

# 3. Crear controles individuales en la barra lateral
if seleccion:
    st.sidebar.header("Configurar Objetivos")
    for ticker in seleccion:
        st.sidebar.subheader(f"📍 {ticker}")
        p_min = st.sidebar.number_input(f"Precio Compra (Mín) - {ticker}", value=0.0, key=f"min_{ticker}")
        p_max = st.sidebar.number_input(f"Precio Venta (Máx) - {ticker}", value=1000.0, key=f"max_{ticker}")
        limites[ticker] = {"min": p_min, "max": p_max}

# 4. Procesar y mostrar cada acción
for ticker in seleccion:
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="5d")
        
        if not df.empty:
            precio = df['Close'].iloc[-1]
            objetivo_min = limites[ticker]["min"]
            objetivo_max = limites[ticker]["max"]
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # Lógica de Alertas Individuales
                if precio >= objetivo_max:
                    st.info(f"💎 ¡OBJETIVO ALCANZADO!\n{ticker}: {precio:.2f}")
                    st.balloons() # Celebra cuando llega al precio de venta
                elif precio <= objetivo_min and objetivo_min > 0:
                    st.error(f"⚠️ ¡BAJO EL MÍNIMO!\n{ticker}: {precio:.2f}")
                else:
                    st.success(f"✅ {ticker}: {precio:.2f}")
                
                st.caption(f"Rango: {objetivo_min} - {objetivo_max}")
            
            with col2:
                st.line_chart(df['Close'], height=120)
                
    except Exception:
        st.error(f"Error al cargar {ticker}")
