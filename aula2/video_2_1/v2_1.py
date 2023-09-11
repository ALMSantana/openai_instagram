import openai
from dotenv import load_dotenv
import os

def openai_gpt_resumir_texto(transcricao_completa, nome_arquivo, openai):
    print("Resumindo com o gpt para um post do instagram ...")

    prompt_sistema = """
    Assuma que você é um digital influencer digital e que está construíndo conteúdos das áreas de tecnologia em uma plataforma de áudio (podcast).

    Os textos produzidos devem levar em consideração uma peresona que consumirá os conteúdos gerados. Leve em consideração:

    - Seus seguidores são pessoas super conectadas da área de tecnologia, que amam consumir conteúdos relacionados aos principais temas da área de computação.
    - Você deve utilizar o gênero neutro na construção do seu texto
    - Os textos serão utilizados para convidar pessoas do instagram para consumirem seu conteúdo de áudio
    - O texto deve ser escrito em português do Brasil.

    """
    prompt_usuario = ". \nReescreva a transcrição acima para que possa ser postado como uma legenda do Instagram. Ela deve resumir o texto para chamada na rede social. Inclua hashtags"

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content" : prompt_sistema
            },
            {
                "role": "user",
                "content": transcricao_completa + prompt_usuario
            }
        ],
        temperature = 0.6
    )

    resumo_instagram = resposta["choices"][0]["message"]["content"]

    with open(f"resumo_instagram_{nome_arquivo}.txt", "w",encoding='utf-8') as arquivo_texto:
        arquivo_texto.write(resumo_instagram)

    return resumo_instagram