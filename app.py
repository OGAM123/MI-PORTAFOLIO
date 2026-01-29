import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Mi Portafolio Pro", page_icon="💰")
st.title("📈 Mi Rastreador con Alertas de Venta")

# 1. Lista de acciones
tickers_disponibles = ["AAPL", "NVDA", "BACKUSI1.LM", "ALICORC1.LM", "TTD", "INRETC1.LM", "BBVAC1.LM", "ORYGENC1.LM", "SPHQ", "AUNA.LM", "KO"]

# 2. Selección de acciones
seleccion = st.multiselect("Selecciona tus acciones:", tickers_disponibles, default=["AAPL"])

# 3. Configuración de Alertas Globales (puedes personalizarlas por acción luego)
st.sidebar.header("Configuración de Alertas")
min_alerta = st.sidebar.number_input("Alerta de Compra (Precio Mínimo)", value=10.0)
max_alerta = st.sidebar.number_input("Alerta de Venta (Precio Máximo)", value=200.0)

for ticker in seleccion:
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="5d")
        
        if not df.empty:
            precio = df['Close'].iloc[-1]
            
            # Lógica de Alertas
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if precio >= max_alerta:
                    st.info(f"💎 ¡VENTA! {ticker}: {precio:.2f}")
                    st.balloons() # ¡Efecto de globos al llegar al máximo!
                elif precio <= min_alerta:
                    st.error(f"⚠️ ¡COMPRA! {ticker}: {precio:.2f}")
                else:
                    st.success(f"✅ {ticker}: {precio:.2f}")
            
            with col2:
                st.line_chart(df['Close'], height=100)
    except Exception:
        st.error(f"Error con {ticker}")
