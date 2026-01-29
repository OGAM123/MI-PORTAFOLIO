import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Mi Portafolio", page_icon="💰")

st.title("🚀 Mi Rastreador de Inversiones")

# 1. LISTA DE ACCIONES (Asegúrate de que AAPL esté para que no dé error)
tickers_disponibles = [
    "AAPL", "NVDA", "BACKUSI1.LM", "ALICORC1.LM", "TTD", 
    "INRETC1.LM", "BBVAC1.LM", "ORYGENC1.LM", 
    "SPHQ", "AUNA.LM", "KO"
]

# 2. SELECCIÓN DE USUARIO
seleccion = st.multiselect("Selecciona tus acciones:", tickers_disponibles, default=["AAPL"])

# 3. CONFIGURAR ALERTA
umbral = st.number_input("Avísame si baja de:", value=10.0)

# 4. PROCESAR CADA ACCIÓN
for ticker in seleccion:
    try:
        stock = yf.Ticker(ticker)
        # Obtenemos los últimos datos de precio
        hist = stock.history(period="1d")
        
        if not hist.empty:
            # Esta línea extrae el precio de cierre más reciente
            precio = hist['Close'].iloc[-1]
            
            col1, col2 = st.columns([1, 2])
            with col1:
                if precio < umbral:
                    st.error(f"⚠️ {ticker}: {precio:.2f}")
                else:
                    st.success(f"✅ {ticker}: {precio:.2f}")
            with col2:
                # Gráfico de 5 días
                hist_grafico = stock.history(period="5d")
                st.line_chart(hist_grafico['Close'], height=100)
        else:
            st.warning(f"No hay datos hoy para {ticker} (Bolsa cerrada o nombre incorrecto)")
                
    except Exception as e:
        st.error(f"Error cargando {ticker}")
