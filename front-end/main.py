import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

def getStatus(taxa):
    if taxa < 50:
        return "Normal"
    else:
        return "Alto"

def showGraph(data):
    df = pd.DataFrame(data)
    
    if not df.empty:
        plt.figure(figsize=(10, 5))
        plt.bar(df['nome'], df['taxa'], color='blue')
        plt.xlabel('Nome')
        plt.ylabel('Taxa de Trafego')
        plt.title('Taxa de Trafego por Dispositivo')
        st.pyplot(plt)

def showTable(data):
    df = pd.DataFrame(data)
    df["Status"] = df["taxa"].apply(getStatus)

    for index, row in df.iterrows():
        col1, col2, col3, col4 = st.columns(4)
        col1.write(row["ip"])
        col2.write(row["nome"])
        col3.write(f"{row['taxa']} Mbps")
        if row["Status"] == "Alto":
            col4.markdown('<span style="color:red;">Alto</span>', unsafe_allow_html=True)
        else:
            col4.markdown('<span style="color:green;">Normal</span>', unsafe_allow_html=True)
        
        # Botão de remover
        if col4.button("Remover", key=f"remove_{index}"):
            delete_url = f"http://localhost:8080/dispositivos/{row['id']}"  # URL com o ID do dispositivo
            delete_response = requests.delete(delete_url)
            if delete_response.status_code == 204:
                st.success(f"Dispositivo {row['nome']} removido com sucesso!")
                # Atualiza os dados após a remoção
                st.session_state["data"] = fetch_data()  # Atualiza os dados na sessão
            else:
                st.error(f"Erro ao remover o dispositivo {row['nome']}.")

def fetch_data():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Erro ao obter os dados.")
        return []

st.write("Monitoramento do trafego de rede")
ip = st.text_input("Endereco IP do dispositivo")
nome = st.text_input("Nome")
taxaTrafego = st.number_input("Taxa de trafego")
button = st.button("Registrar")

url = "http://localhost:8080/dispositivos"

# Atualiza os dados apenas se o botão for clicado
if button:
    if ip and nome and taxaTrafego:
        data = {
            "ip": ip,
            "nome": nome,
            "taxa": taxaTrafego
        }
        response = requests.post(url, json=data)
        if response.status_code == 201:
            st.success("Dispositivo registrado com sucesso!")
        else:
            st.error("Erro ao registrar dispositivo.")
    else:
        st.error("Preencha todos os campos.")

# Inicializa os dados na sessão
if "data" not in st.session_state:
    st.session_state["data"] = fetch_data()

# Exibe o gráfico e a tabela com os dados atualizados
showGraph(st.session_state["data"])
showTable(st.session_state["data"])