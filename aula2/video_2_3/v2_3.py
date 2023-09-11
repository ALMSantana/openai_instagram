import openai
from dotenv import load_dotenv
import os

def openai_gpt_gerar_texto_imagem(resumo_instagram, nome_arquivo, openai):
    print("Gerando a saida de texto para criacao de imagens com o GPT ...")

    prompt_sistema = """

    - A saída deve ser uma única, do tamanho de um tweet, que seja capaz de descrever o conteúdo do texto para que possa ser transcrito como uma imagem.
    - Não inclua hashtags

    """

    prompt_usuario =  f'Reescreva o texto a seguir, em uma frase, para que descrever o texto abaixo em um tweet: {resumo_instagram}'
    
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content" : prompt_sistema
            },
            {
                "role": "user",
                "content": prompt_usuario
            }
        ],
        temperature = 0.6
    )

    texto_para_imagem = resposta["choices"][0]["message"]["content"]

    with open(f"texto_para_geracao_imagem_{nome_arquivo}.txt", "w",encoding='utf-8') as arquivo_texto:
        arquivo_texto.write(texto_para_imagem)
    
    return texto_para_imagem