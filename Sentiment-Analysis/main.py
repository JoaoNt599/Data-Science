import subprocess
import uvicorn
import os
import sys


def start_streamlit():
    """
    Função para iniciar o Streamlit.
    Define a variável de ambiente para o host do FastAPI e executa o comando para iniciar o Streamlit.
    """

    # Evita prompt de email e abre automático no navegador
    os.environ["STREAMLIT_SUPPRESS_BROWSER_OPEN"] = "false"

    # Define a variável de ambiente para o host do FastAPI
    os.environ['FASTAPI_HOST'] = 'localhost'

    # Usa o comando streamlit diretament
    subprocess.Popen(["streamlit", "run", "frontend/streamlit.py"])


if __name__ == "__main__":

    # Adiciona o diretório raiz do projeto ao PYTHONPATH
    sys.path.append(os.getcwd())
    sys.path.append(os.path.join(os.getcwd(), 'backend'))

    # Inicia o Streamlit
    start_streamlit()
    
    # Executa o servidor Uvicorn para a aplicação FastAPI
    uvicorn.run("backend.fast_api:app", host="0.0.0.0", port=8000, reload=True)





