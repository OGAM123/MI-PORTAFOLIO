import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Mi Portafolio", page_icon="💰")

st.title("🚀 Mi Rastreador de Inversiones")
st.write("Configura tus acciones y recibe alertas.")

# Lista de tickers (asegúrate de que terminen en .LM si son de la bolsa de Lima, ej: ALICORC1.LM)
tickers_ejemplo = ["BACKUSI1.LM", "NVDA", "ALICORC1.LM", "TTD", "INRETC1.LM", "BBVAC1.LM", "ORYGENC1.LM", "SPHQ", "AUNA.LM", "KO"]
mis_acciones = st.multiselect("Selecciona tus acciones:", tickers_ejemplo, default=["AAPL"])

umbral = st.number_input("Avísame si alguna baja de ($):", value=10.0)

for ticker in mis_acciones:
    try:
        datos = yf.Ticker(ticker)
        # Intentamos obtener el precio de forma segura
        precio = datos.fast_info.get('last_price', None)
        
        if precio is not None:
            col1, col2 = st.columns([1, 3])
            with col1:
                if precio < umbral:
                    st.error(f"⚠️ {ticker}: ${precio:.2f}")
                else:
                    st.success(f"✅ {ticker}: ${precio:.2f}")
            with col2:
                hist = datos.history(period="5d")
                if not hist.empty:
                    st.line_chart(hist['Close'], height=100)
        else:
            st.warning(f"No se encontró precio para {ticker}. Revisa el nombre.")
            
    except Exception as e:
        st.error(f"Error con {ticker}: {e}")
