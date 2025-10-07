import streamlit as st 
import requests
import os
from pymongo import MongoClient


# Configs
API_URL = "http://fastapi:8000"
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/")

mongo_client = MongoClient(MONGO_URI)
db = mongo_client["local"]
feedback_collection = db["feedback"]

# Inicializa o estado da sessão
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "token" not in st.session_state:
    st.session_state.token = None


# Tela de login
def login():
    st.title("Login")

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        response = requests.post(f"{API_URL}/login", json={"username": username, "password": password})

        if response.status_code == 200:
            data = response.json()
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.token = data["access_token"]
            st.success("Login realizado com sucesso!")
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos.")


# Tela principal protegida
def app_principal():
    st.title("Input de Comentários - Análise de Sentimentos")

    # Botão de logout
    if st.button("Sair"):
        st.session_state.clear()
        st.success("Logout efetuado.")
        st.rerun()

    tab1, tab2 = st.tabs(["Enviar Comentário", "Ver Feedbacks"])

    with tab1:
        comment = st.text_input("Escreva seu comentário:")
        rating = st.slider("Avaliação (1 a 5 estrelas):", 1, 5, 3)

        if st.button("Enviar Comentário"):
            headers = {"Authorization": f"Bearer {st.session_state.token}"}
            response = requests.post(
                f"{API_URL}/feedback/",
                json={"comment": comment, "rating": rating},
                headers=headers
            )

            if response.status_code == 200:
                feedback = response.json()
                st.write(f"**Você comentou:** {comment}")
                st.write(f"**Avaliação:** {rating} estrelas")
                st.write(f"**Feedback:** {feedback['descricao']}")
                status_color = "green" if feedback['status'] == "aprovado" else "red"
                st.markdown(f"**Status:** <span style='color:{status_color}'>{feedback['status']}</span>", unsafe_allow_html=True)
            else:
                try:
                    error = response.json()
                    st.error(f"Erro ao enviar comentário: {error.get('detail')}")
                except Exception:
                    st.error("Erro ao enviar comentário.")

    with tab2:
        st.subheader("Feedbacks Salvos")
        for fb in feedback_collection.find():
            st.write(f"**ID:** {fb.get('_id')}")
            st.write(f"**Comentário:** {fb['comment']}")
            st.write(f"**Avaliação:** {fb['rating']} estrelas")
            st.write(f"**Sentimento:** {fb.get('descricao')}")
            st.write(f"**Status:** {fb.get('status', 'Não disponível')}")
            st.write("---")


# Roteador principal
def main():
    if st.session_state.logged_in:
        app_principal()
    else:
        login()


if __name__ == "__main__":
    main()
