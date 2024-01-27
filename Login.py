import streamlit as st
from pymongo import MongoClient
from bson import ObjectId
import hashlib




# Conectar ao banco de dados MongoDB
client = MongoClient('mongodb+srv://user_01:sucesso1807@cluster0.slfd3no.mongodb.net/')
db = client['user_01-hnokt']
usuarios_colecao = db['login']



    
import streamlit as st
st.set_page_config(page_title="Tela de Login", 
                page_icon=":lock:", layout="centered")

st.title("Tela de Login")
st.subheader("Sérgio Santos  - Cursos e treinamentos")

def main():
    st.title("Acesso nosso Sistema")

    # Adicione campos para inserir nome de usuário e senha
    username = st.text_input("Nome de Usuário:")
    password = st.text_input("Senha:", type="password")

    # Adicione um botão para fazer login
    if st.button("Login"):
        if autenticar_usuario(username, password):
            
            st.info("Bem-vindo(a) ao nosso curso, " + username + "!")
            st.video("https://www.youtube.com/watch?v=QwievZ1Tx-8")
            st.balloons() 
            
            
        else:
            st.error("Usuário não encontrado. Tente novamente.")

def autenticar_usuario(username, password):
    # Criptografe a senha antes de comparar com o banco de dados
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Tente encontrar o usuário no MongoDB
    usuario = usuarios_colecao.find_one({"username": username, "password": hashed_password})
    return usuario is not None



    

if __name__ == "__main__":
    main()




        

        
        
        # ESTE CÓDIGO LIMPA O BANCO DE DADOS MONGODB
# # Limpar dados do MongoDB (Apenas para fins de teste. Não use isso em produção!)
# if st.button("Limpar Dados MongoDB"):
#     usuarios_colecao.delete_many({})
#     st.warning("Dados do MongoDB apagados para fins de teste.")


