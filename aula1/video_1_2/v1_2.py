import openai
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    caminho_audio = "podcasts/hipsters_154_testes_short.mp3"
    nome_arquivo = "hipsters_154_testes_short"
    url_podcast = "https://www.hipsters.tech/testes-de-software-e-inteligencia-artificial-hipsters-154/"
    
    api_openai = os.getenv("API_KEY_OPENAI")
    openai.api_key = api_openai

if __name__ == "__main__":
    main()  
