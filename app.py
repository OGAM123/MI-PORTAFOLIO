import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Mi Portafolio", page_icon="💰")
st.title("🚀 Mi Rastreador de Inversiones")

# Lista de acciones ajustada
tickers_disponibles = [
    "AAPL", "NVDA", "BACKUSI1.LM", "ALICORC1.LM", "TTD", 
    "INRETC1.LM", "BBVAC1.LM", "ORYGENC1.LM", 
    "SPHQ", "AUNA.LM", "KO"
]

seleccion = st.multiselect("Selecciona tus acciones:", tickers_disponibles, default=["AAPL"])
umbral = st.number_input("Avísame si baja de:", value=10.0)

for ticker in seleccion:
    try:
        stock = yf.Ticker(ticker)
        # Traemos los últimos 5 días para asegurar que haya al menos un precio
        df = stock.history(period="5d")
        
        if not df.empty:
            # Tomamos el último precio de cierre que no sea vacío
            precio = df['Close'].iloc[-1]
            
            col1, col2 = st.columns([1, 2])
            with col1:
                if precio < umbral:
                    st.error(f"⚠️ {ticker}: {precio:.2f}")
                else:
                    st.success(f"✅ {ticker}: {precio:.2f}")
            with col2:
                st.line_chart(df['Close'], height=100)
        else:
            st.warning(f"Buscando datos para {ticker}...")
                
    except Exception:
        st.error(f"Error con {ticker}")
