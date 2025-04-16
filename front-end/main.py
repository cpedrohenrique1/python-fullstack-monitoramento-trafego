import streamlit as st
import pandas as pd
import requests

st.write("Monitoramento do trafego de rede")
ip = st.text_input("Endereco IP do dispositivo")
nome = st.text_input("Nome")
taxa_trafego = st.number_input("Taxa de trafego")
button = st.button("Registrar")
url = "./test.json"
response = pd.read_json(url)

if not response.empty:
    st.write("Dispositivos registrados")
    st.bar_chart(response)