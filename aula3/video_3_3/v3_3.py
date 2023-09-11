import openai
from dotenv import load_dotenv
import os
import requests
from pydub import AudioSegment

def ferramenta_transcrever_audio_em_partes(caminho_audio_podcast, nome_arquivo):
    print("Iniciando corte .. ")
    audio = AudioSegment.from_mp3(caminho_audio_podcast)

    dez_minutos = 10 * 60 * 1000
    
    contador_pedaco = 1
    arquivos_exportados = []

    while len(audio) > 0:
        pedaco = audio[:dez_minutos]
        nome_pedaco_audio = f"{nome_arquivo}_parte_{contador_pedaco}.mp3"
        pedaco.export(nome_pedaco_audio, format="mp3")
        arquivos_exportados.append(nome_pedaco_audio)
        audio = audio[dez_minutos:]
        contador_pedaco += 1

    return arquivos_exportados

def openai_whisper_transcrever_em_partes(caminho_audio, nome_arquivo, modelo_whisper, openai):
    print("Estou transcrevendo com o whispers ...")

    lista_arquivos_de_audio = ferramenta_transcrever_audio_em_partes(caminho_audio, nome_arquivo)
    lista_pedacos_de_audio = []

    for um_pedaco_audio in lista_arquivos_de_audio:
        audio = open(um_pedaco_audio, "rb")

        resposta = openai.Audio.transcribe(
            api_key=openai.api_key,
            model = modelo_whisper,
            file = audio
        )

        transcricao = resposta.text
        lista_pedacos_de_audio.append(transcricao)
    
    transcricao = "".join(lista_pedacos_de_audio)

    with open(f"texto_completo_{nome_arquivo}.txt", "w",encoding='utf-8') as arquivo_texto:
        arquivo_texto.write(transcricao)

    return transcricao