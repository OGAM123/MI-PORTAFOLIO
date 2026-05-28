import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Mi Portafolio Alertas", page_icon="💰")
st.title("📈 Monitor con Alertas Guardadas")

# 1. DEFINE AQUÍ TUS PRECIOS (Esto no se borrará al cerrar la app)
# Formato: "TICKER": [Precio Mínimo, Precio Máximo]
mis_objetivos = {
    "INRETC1.LM": [26.0, 38.0],
    "NVDA": [180.0, 260.0],
    "BBVAC1.LM": [2.0, 2.21],
    "ALICORC1.LM": [10.50, 12.50],
    "BACKUSI1.LM": [20.0, 28.0],
    "TTD": [30.0, 60.0],
    "KO": [69.0, 79.0],
    "ENGEPEC1.LM": [2.75, 3.30],
    "AUNA": [5.4, 8.70],
    "SPHQ": [77.75, 100.70],
    "CREDITC1.LM": [6.0, 7.30],
    "BTC-USD": [73300.0, 110000.0]
    }
# Crea un diccionario para "traducir" los nombres en la pantalla
nombres_pantalla = {
    "EGEPEC1.LM": "ORYGENC1"
      }

# Luego, cuando imprimas el nombre en Streamlit, usa:
# st.write(f"Acción: {nombres_pantalla.get(ticker, ticker)}")
seleccion = st.multiselect("Acciones en vigilancia:", list(mis_objetivos.keys()), default=["NVDA"])

for ticker in seleccion:
    try:
        stock = yf.Ticker(ticker)
        # Cambiamos a period="max" o "1mo" y añadimos repair=True para que yfinance intente arreglar el error
        df = stock.history(period="1mo", raise_errors=False)
        
        if not df.empty:
            precio = df['Close'].iloc[-1]
            p_min = mis_objetivos[ticker][0]
            p_max = mis_objetivos[ticker][1]
            
            col1, col2 = st.columns([1, 2])
            with col1:
                if precio >= p_max:
                    st.info(f"💎 ¡VENTA! {ticker}\nLlegó a: {precio:.2f}")
                    st.balloons()
                elif precio <= p_min:
                    st.error(f"⚠️ ¡COMPRA! {ticker}\nLlegó a: {precio:.2f}")
                else:
                    st.success(f"✅ {ticker}: {precio:.2f}")
                   
                st.caption(f"Rango definido: {p_min} - {p_max}")
            with col2:
                st.line_chart(df['Close'], height=120)
    except:
        st.error(f"❌ Error técnico con {ticker}: Yahoo no responde.")
