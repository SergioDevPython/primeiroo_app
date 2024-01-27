import streamlit as st





# Dados simulados de videoaulas (você pode substituir por dados reais do seu aplicativo)
videoaulas = {
    "Aula 1": "https://www.youtube.com/watch?v=WfLZUx4NC7U&ab_channel=CortesdoCi%C3%AAnciaSemFim%5BOFICIAL%5D",
    "Aula 2": "https://www.youtube.com/watch?v=UZcn4OF8fKA&ab_channel=LucasMontano",
    "Aula 3": "https://www.youtube.com/watch?v=UtkPIpov6h8&ab_channel=DevAprender%7CJhonatandeSouza",
}

def video_aulas():
    st.title("Programa de Videoaulas")

    # Sidebar com a lista de videoaulas
    aula_selecionada = st.sidebar.selectbox("Demo", list(videoaulas.keys()))

    # Exibindo o título da aula selecionada
    st.header(aula_selecionada)

    # Obtendo o link do vídeo da aula selecionada
    link_video = videoaulas[aula_selecionada]

    # Incorporando o vídeo no Streamlit
    st.video(link_video)

if __name__ == "__main__":
    video_aulas()
