import requests

def search_email(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"User-Agent": "OSINT Tracker"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print(f"[!] E-mail comprometido: {email}")
    else:
        print(f"[+] Nenhum registro encontrado para: {email}")

if __name__ == "__main__":
    target_email = input("Digite o e-mail alvo: ")
    search_email(target_email)
