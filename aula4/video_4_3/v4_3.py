import openai
from dotenv import load_dotenv
import os
import requests
from pydub import AudioSegment
from PIL import Image
import shutil
from instabot import Bot

def postar_instagram(caminho_imagem, texto, user, password):
    if os.path.exists("config"):
        shutil.rmtree("config")
    bot = Bot()
    
    bot.login(username=user, password=password)

    resposta = bot.upload_photo(caminho_imagem, caption=texto)

