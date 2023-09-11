import openai
from dotenv import load_dotenv
import os
import requests


def openai_dalle_gerar_imagem(resolucao, resumo_para_imagem, nome_arquivo, openai, qtd_imagens = 1):
    print("Criando uma imagem utilizando a API do DALL-E ...")

    prompt_user = f"Uma pintura ultra futurista, textless, 3d que retrate: {resumo_para_imagem}"
    
    resposta = openai.Image.create(
        prompt =prompt_user,
        n = qtd_imagens,
        size = resolucao
    )

    print(resposta["data"][0].url)
    return resposta["data"]

