import openai
from dotenv import load_dotenv
import os
import requests


def ferramenta_download_imagem(nome_arquivo, imagem_gerada,qtd_imagens = 1):
  lista_nome_imagens = []
  try:
    for contador_imagens in range(0,qtd_imagens):
        camimho = imagem_gerada[contador_imagens].url
        imagem = requests.get(camimho)

        with open(f"{nome_arquivo}_{contador_imagens}.png", "wb") as arquivo_imagem:
            arquivo_imagem.write(imagem.content)

        lista_nome_imagens.append(f"{nome_arquivo}_{contador_imagens}.png")
    return lista_nome_imagens
  except:
    print("Ocorreu um erro!")
    return  None

def openai_dalle_gerar_imagem(resolucao, resumo_para_imagem, nome_arquivo, openai, qtd_imagens = 1):
    print("Criando uma imagem utilizando a API do DALL-E ...")

    prompt_user = f"Uma pintura ultra futurista, textless, 3d que retrate: {resumo_para_imagem}"
    
    resposta = openai.Image.create(
        prompt =prompt_user,
        n = qtd_imagens,
        size = resolucao
    )

    return resposta["data"]
