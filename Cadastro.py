import streamlit as st
import pandas as pd
from datetime import date


def gravar_dados(nome, dataNasc, tipoCliente):
    if nome and dataNasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file: #Configurações do arquivo
            file.write(f"{nome},{dataNasc},{tipoCliente} \n") #IMPORTANTE, SEMPRE PASSAR OS ATRIBUTOS DE ACORDO COM O BANCO, COLOCAR \n PARA QUEBRAR LINHA.
        st.session_state["Sucesso"] = True
    else:
        st.session_state["Sucesso"] = False


st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="🛒"
)

st.title("Cadastro de clientes")
st.divider()  #Colocando uma linha embaixo

nome = st.text_input("Digite o nome do cliente" , 
                     key="nome_cliente")

dataNasc = st.date_input("Data de nascimento", format="DD/MM/YYYY")

tipoCliente = st.selectbox("Tipo do cliente",
                           ["Pessoa Jurídica", "Pessoa Física"])

botaoCadastrar = st.button("Cadastrar", 
                           on_click=gravar_dados,
                           args=[nome, dataNasc, tipoCliente])

if botaoCadastrar:
    if st.session_state["Sucesso"]:
        st.success("Cliente Cadastrado Com Sucesso!", icon="✔")
    else:
        st.error("Houve algum problema ao cadastrar o cliente", icon="💢")