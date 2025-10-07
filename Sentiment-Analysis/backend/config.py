from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do .env 
load_dotenv()

def str_to_bool(value):
    return value.lower() in ('true', '1', 't', 'y', 'yes')

API_KEY = os.getenv('') # API KEY
DATABASE_NAME = 'local'
MOCK_OPENAPI_SERVICE = str_to_bool(os.getenv('MOCK_OPENAPI_SERVICE', 'TRUE'))