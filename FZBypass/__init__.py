from os import getenv
from time import time
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.enums import ParseMode
from logging import getLogger, FileHandler, StreamHandler, INFO, ERROR, basicConfig
from uvloop import install

install()
basicConfig(format="[%(asctime)s] [%(levelname)s] - %(message)s", #  [%(filename)s:%(lineno)d]
            datefmt="%d-%b-%y %I:%M:%S %p",
            handlers=[FileHandler('log.txt'), StreamHandler()],
            level=INFO)

getLogger("pyrogram").setLevel(ERROR)
LOGGER = getLogger(__name__)

load_dotenv('config.env', override=True)
BOT_START = time()

class Config:
    BOT_TOKEN = getenv('BOT_TOKEN', '6982026238:AAFaNNSp3XPLO5Ol25Hu3pYnLK9EmkJwXMo')
    API_HASH  = getenv('API_HASH', 'c216393ab439dd055858680916a3444b')
    API_ID    = getenv('API_ID', '16023154')
    if BOT_TOKEN == '' or API_HASH == '' or API_ID == '':
        LOGGER.critical('ENV Missing. Exiting Now...')
        exit(1)
    AUTO_BYPASS     = getenv('AUTO_BYPASS', 'True').lower() == 'true'
    AUTH_CHATS      = getenv('AUTH_CHATS', '-1001920596580').split()
    OWNER_ID        = int(getenv('OWNER_ID', 1397269319))
    DIRECT_INDEX    = getenv('DIRECT_INDEX', 'https://gitlab.com/GoogleDriveIndex/cloudflare-gdrive-download-worker/-/raw/main/src/worker.js?ref_type=heads').rstrip('/')
    LARAVEL_SESSION = getenv('LARAVEL_SESSION', '')
    XSRF_TOKEN      = getenv('XSRF_TOKEN', '')
    GDTOT_CRYPT     = getenv('GDTOT_CRYPT', '')
    DRIVEFIRE_CRYPT = getenv('DRIVEFIRE_CRYPT', '')
    HUBDRIVE_CRYPT  = getenv('HUBDRIVE_CRYPT', '')
    KATDRIVE_CRYPT  = getenv('KATDRIVE_CRYPT', '')
    UPTOBOX_TOKEN   = getenv('UPTOBOX_TOKEN', '')
    TERA_COOKIE     = getenv('TERA_COOKIE', '')

Bypass = Client("FZ", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN, plugins=dict(root="FZBypass/plugins"), parse_mode=ParseMode.HTML)
