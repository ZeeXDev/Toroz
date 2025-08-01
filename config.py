#Cluster0luster0 Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7959446467:AAED1D7vvmY7PQbn2y2B6cHbVxBX6vm2InQ")
APP_ID = int(os.environ.get("APP_ID", "25926022")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "30db27d9e56d854fb5e943723268db32") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002665318918")) #Your db channel Id
OWNER = os.environ.get("OWNER", "ZeeXDevBot") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "8140299716")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://tgbot:4KzEdxEl4YldwwFR@tg.vr8ef.mongodb.net/?retryWrites=true&w=majority&appName=Tg")
DB_NAME = os.environ.get("DATABASE_NAME", "Tg")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "60"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/BTZF_CHAT")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://iili.io/FakDfLu.md.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://iili.io/Fc0oBrF.md.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>Ceci est un bot de lien de fichier pour @Godanimes & @serieetfilmsvfnet\n\n❏ Commandes du bot\n├/start : Démarrer le bot\n├/about : Nos informations\n└/help : Aide relative au bot\n\nCliquez simplement sur le lien et démarrez le bot. Rejoignez les deux canaux et réessayez, c'est tout... !\n\nDéveloppé par <a href=https://t.me/ZeeXDev>Kingcey</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ Créateur : <a href='https://t.me/ZeeXDevBot'>Kingcey</a>\n◈ Fondateur de : <a href='https://t.me/ZeeXClub'>ZeeXClub</a>\n◈ Chaîne d'anime : <a href='https://t.me/Godanimes'>♨️ 𝗔𝗻𝗶𝗺𝗲 𝗚𝗼𝗱</a>\n◈ Chaîne de séries : <a href='https://t.me/serieetfilmsvfnet'>Séries & films Vf Net</a>\n◈ Vos Bots : <a href='https://t.me/ZeeXDev'>ZeeXDev</a>\n◈ Développeur : <a href='https://t.me/ZeeXDev'>Kingcey</a></blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>Salut {first}\n\n<blockquote>I'm Ano, je suis là pour vous aider à récupérer vos fichiers via un lien spécial.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Salut {first}\n\n<b>Rejoignez nos canaux puis cliquez sur le bouton Recharger pour obtenir le fichier demandé.</b>")

CMD_TXT = """<blockquote><b>» Commandes administrateur :</b></blockquote>

<b>›› /dlt_time :</b> Définir le temps de suppression automatique
<b>›› /check_dlt_time :</b> Vérifier le temps de suppression actuel
<b>›› /dbroadcast :</b> Diffuser un document/vidéo
<b>›› /ban :</b> Bannir un utilisateur
<b>›› /unban :</b> Débannir un utilisateur
<b>›› /banlist :</b> Obtenir la liste des utilisateurs bannis
<b>›› /addchnl :</b> Ajouter un canal d'abonnement obligatoire
<b>›› /delchnl :</b> Supprimer un canal d'abonnement obligatoire
<b>›› /listchnl :</b> Voir les canaux ajoutés
<b>›› /fsub_mode :</b> Activer/désactiver le mode abonnement obligatoire
<b>›› /pbroadcast :</b> Envoyer une photo à tous les utilisateurs
<b>›› /add_admin :</b> Ajouter un administrateur
<b>›› /deladmin :</b> Supprimer un administrateur
<b>›› /custom_batch : </b> Batch personnalisée</b>
<b>›› /pbroadcast : pour envoyer un message à épinglé
<b>›› /dbroadcast : pour envoyer un message éphémere aux utilisateurs
<b>›› /admins :</b> Obtenir la liste des administrateurs
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b><blockquote>• @ZeeXDev</blockquote></b>") #Définissez votre légende personnalisée ici, mettez None pour désactiver
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #Mettez True si vous voulez empêcher le transfert de fichiers depuis le bot
#--------------------------------------------
#Mettez True si vous voulez désactiver le bouton de partage des posts du canal
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>TEMPS DE FONCTIONNEMENT DU BOT</b>\n{uptime}"
USER_REPLY_TEXT = "Bakka ! Tu n'es pas mon senpai !!"
#--------------------------------------------


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
