import hashlib
import requests

def check_breach(password: str) -> int:
    sha1_pw = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_pw[:5]
    suffix = sha1_pw[5:]

    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")

    if response.status_code != 200:
        return -1

    hashes = (line.split(":") for line in response.text.splitlines())

    for h, count in hashes:
        if h == suffix:
            return int(count)

    return 0
