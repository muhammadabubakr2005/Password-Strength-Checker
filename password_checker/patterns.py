import re

COMMON_PATTERNS = [
    r"1234", r"qwerty", r"password", r"abcd", r"1111", r"aaaa"
]

def detect_patterns(password: str):
    issues = []

    for pattern in COMMON_PATTERNS:
        if re.search(pattern, password.lower()):
            issues.append(f"Contains common pattern: {pattern}")

    if re.search(r"(.)\1{2,}", password):
        issues.append("Contains repeated characters (aaa, 111).")

    return issues
