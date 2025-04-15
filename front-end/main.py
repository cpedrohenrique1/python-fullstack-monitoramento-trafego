import streamlit as st
import pandas as pd

st.write("Monitoramento do trafego de rede")
ip = st.text_input("Registro de dispositivo")
nome = st.text_input("Nome")
button = st.button("Registrar")

if (button):
    st.write("Dispositivos registrados")
    df = pd.read_json("/app/front-end/test.json")
    st.line_chart(df)