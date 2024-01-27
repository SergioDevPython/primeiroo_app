import streamlit as st
from pymongo import MongoClient
import hashlib



# Configuração do MongoDB
client = MongoClient('mongodb+srv://user_01:sucesso1807@cluster0.slfd3no.mongodb.net/')
db = client['user_01-hnokt']
usuarios_colecao = db['login']




def cadastrar_usuario(username, password):
    # Verifique se o usuário já existe no MongoDB
    if usuarios_colecao.find_one({"username": username}):
        st.error("Usuário já cadastrado. Escolha outro nome de usuário.")
    else:
        # Criptografe a senha antes de armazená-la
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        def gen_hash_key(key):
            return hashlib.sha256(key.encode()).digest()
        # Insira o novo usuário no MongoDB
        usuarios_colecao.insert_one({
            "username": username,
            "password": hashed_password
        })
        st.success("Cadastro bem-sucedido!")

def main():
    st.title("Cadastro de Pessoas com MongoDB")

    # Adicione campos para inserir nome de usuário e senha
    novo_usuario = st.text_input("Novo Usuário:")
    nova_senha = st.text_input("Nova Senha:", type="password")

    # Adicione um botão para cadastrar um novo usuário
    if st.button("Cadastrar"):
        cadastrar_usuario(novo_usuario, nova_senha)

if __name__ == "__main__":
    main()
