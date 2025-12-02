import os

def load_dictionary(path: str):
    if not os.path.exists(path):
        print("⚠️ Dictionary file missing:", path)
        return set()
    
    with open(path, "r", encoding="latin-1") as f:
        return {line.strip().lower() for line in f}

def is_common_password(password: str, dictionary: set) -> bool:
    return password.lower() in dictionary
