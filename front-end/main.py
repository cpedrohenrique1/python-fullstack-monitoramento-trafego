import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

url = "http://back-end:8080/dispositivos"

def showGraph(df):
    if not df.empty:
        plt.figure(figsize=(10, 5))
        plt.bar(df['nome'], df['taxa'], color='blue')
        plt.xlabel('Nome')
        plt.ylabel('Taxa de Trafego')
        plt.title('Taxa de Trafego por Dispositivo')
        st.pyplot(plt)

def showTable(df):
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
        
        if col4.button("Remover", key=f"remove_{index}"):
            delete_url = f"{url}/{row['id']}" 
            delete_response = requests.delete(delete_url)
            if delete_response.status_code == 204:
                st.success(f"Dispositivo {row['nome']} removido com sucesso!")
                st.session_state["data"] = getData()
                st.rerun()
            else:
                st.error(f"Erro ao remover o dispositivo {row['nome']}.")

def getStatus(taxa):
    if taxa < 50:
        return "Normal"
    else:
        return "Alto"

def getData():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        if 'taxa' in df.columns:
            df['status'] = df['taxa'].apply(getStatus)
        return df
    else:
        st.error("Erro ao buscar dados do servidor.")
        return pd.DataFrame()

def main():
    st.title("Monitoramento de Dispositivos")
    st.write("Monitoramento do trafego de rede")
    ip = st.text_input("Endereco IP do dispositivo")
    nome = st.text_input("Nome")
    taxaTrafego = st.number_input("Taxa de trafego")
    button = st.button("Registrar")
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
                st.session_state["data"] = getData()
                st.rerun()
            else:
                st.error("Erro ao registrar dispositivo.")
        else:
            st.error("Preencha todos os campos.")
            
    if "data" not in st.session_state:
        st.session_state["data"] = getData()
    
    df = st.session_state["data"]
    if not df.empty:
        showGraph(df)
        showTable(df)
    else:
        st.warning("Nenhum dado disponível.")

if __name__ == "__main__":
    main()