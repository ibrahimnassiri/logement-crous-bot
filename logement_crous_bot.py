import requests
from bs4 import BeautifulSoup
import time

# Configuration
URL = "https://trouverunlogement.lescrous.fr/tools/41/search?bounds=3.8070597_43.6533542_3.9413208_43.5667088"  # ou une page spécifique
TELEGRAM_TOKEN = "7871299052:AAEp0fK1_CKuCBh_zTJFeuth9A0xJ63Dk3c"  # Ton token Bot Telegram
TELEGRAM_CHAT_ID = "6398726956"         # Ton ID Telegram
KEYWORDS = ["CU TRIOLET","CU BOUTONNET", "CU VEYRASSI", "CU VOIE DOMITIENNE","COLOMBIERE" "COLONEL MARCHAND", "CU MINERVE"]

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

def check_site():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text().lower()
    for word in KEYWORDS:
        if word.lower() in text:
            send_telegram_message(f"📢 Logement trouvé ! Mot-clé : {word} \n👉 {URL}")
            break

while True:
    try:
        check_site()
        time.sleep(900)  # Vérifie toutes les 15 minutes
    except Exception as e:
        print("Erreur :", e)
        time.sleep(900)
