import math
import re

def calculate_entropy(password: str) -> float:
    charset = 0

    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[^a-zA-Z0-9]", password): charset += 33

    if charset == 0:
        return 0.0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)
