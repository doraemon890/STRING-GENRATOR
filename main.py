import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("pymongo").setLevel(logging.ERROR)

# Initialize start time
StartTime = time.time()

# Initialize the Client
app = Client(
    "JARVIS",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="SESSIONGEN"),
)

if __name__ == "__main__":
    print("𝙹𝚊𝚛𝚟𝚒𝚜 𝚂𝚎𝚜𝚜𝚒𝚘𝚗 𝙶𝚎𝚗 𝚜𝚝𝚊𝚛𝚝𝚒𝚗𝚐...")
    try:
        app.start()
    except ApiIdInvalid:
        raise Exception("Your API_ID is not valid.")
    except ApiIdPublishedFlood:
        raise Exception("Your API_ID/API_HASH is flood banned.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

    uname = app.get_me().username
    print(f"@{uname} NOW JARVIS SESSION GEN IS READY TO GEN SESSION")
    
    idle()
    
    app.stop()
    print("🇸 🇪 🇸 🇸 🇮 🇴 🇳  🇬 🇪 🇳 🇷 🇦 🇹 🇮 🇳 🇬  🇸 🇹 🇴 🇵 🇵 🇪 🇩...")
