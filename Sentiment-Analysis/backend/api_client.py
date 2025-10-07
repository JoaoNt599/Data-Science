import openai
import json
from config import API_KEY, MOCK_OPENAPI_SERVICE

openai.api_key = API_KEY

# Constante para o prompt
FEEDBACK_VALIDATION_PROMPT = """
Você é um assistente que avalia o sentimento e a opinião comentários recebidos.
Fornecer uma descrição de até 40 palavras descrevendo o sentimento e opiniao capturada do consumidor e um status.
O status deve ser 'aprovado' se o comentário for válido, não tiver tom agressivo ou discriminatorio.
O comentario deve fazer sentido com a avaliação em estrelas
Caso contrário, o status deve ser 'reprovado'.
O retorno deve ser exclusivamente no formato JSON com a seguinte estrutura: 
{
    "descricao": "string",
    "status": "aprovado" ou "reprovado"
}
"""

def get_feedback_from_openai(comentario, avaliacao):

    if not MOCK_OPENAPI_SERVICE:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": FEEDBACK_VALIDATION_PROMPT},
                {"role": "user", "content": f"Comentário: {comentario}\nAvaliação: {avaliacao} estrelas"}
            ]
        )

        feedback_str = response['choices'][0]['message']['content'].strip()

        # Converte a string JSON para um dicionário Python
        feedback_json = json.loads(feedback_str)
    else:
        feedback_json = {
            "descricao": "Não foi possivel avaliar, esse é um resultado padrão do sistema. Ative o serviço de IA para uma análise real.",
            "status": "reprovado"
        }
    
    return feedback_json
