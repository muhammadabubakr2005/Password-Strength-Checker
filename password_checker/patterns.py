import re

COMMON_PATTERNS = [
    # Basic sequences
    r"123", r"1234", r"12345", r"123456", r"111", r"222", r"333",
    r"abc", r"abcd", r"abcdef", r"aaa", r"bbb", r"ccc",

    # Keyboard sequences
    r"qwerty", r"asdf", r"zxcv", r"qaz", r"wsx", r"1q2w3e",

    # Common weak words
    r"password", r"admin", r"letmein", r"welcome", r"iloveyou",
    r"pakistan", r"pak123", r"pass123", r"usman", r"love", r"hello",

    # Variants and leetspeak
    r"p@ss", r"p@ssw0rd", r"p4ss", r"p455", r"l0ve", r"l0ver",

    # Common endings
    r"123$", r"123!", r"@123", r"321", r"786", r"000", r"999",

    # Birth years (1990–2025)
    r"1990", r"1991", r"1992", r"1993", r"1994", r"1995", r"1996",
    r"1997", r"1998", r"1999", r"2000", r"2001", r"2002", r"2003",
    r"2004", r"2005", r"2006", r"2007", r"2008", r"2009", r"2010",
    r"2011", r"2012", r"2013", r"2014", r"2015", r"2016", r"2017",
    r"2018", r"2019", r"2020", r"2021", r"2022", r"2023", r"2024",
    r"2025",

    # Pakistani-specific weak patterns
    r"786", r"pak786", r"pak123", r"lahore", r"karachi", r"islamabad",
    r"admin123", r"admin786", r"pass786", r"hello123",

    # Repetition groups
    r"(.)\1{2,}",  # aaa, 111, !!!, etc.

    # Common name patterns (can expand)
    r"usman", r"ali", r"ahmed", r"ahmad", r"hassan", r"hussain",
]


import re

def detect_patterns(password: str):
    issues = []
    pw = password.lower()

    # Check all common patterns
    for pattern in COMMON_PATTERNS:
        if re.search(pattern, pw):
            issues.append(f"Contains common or predictable pattern: {pattern}")

    # Additional checks
    if re.search(r"(.)\1{2,}", password):
        issues.append("Contains repeated characters (aaa, 111, !!!).")

    # Detect common endings like !, @, 123, @123, 123!, etc.
    if re.search(r"(123|123!|@123|123\$)$", pw):
        issues.append("Ends with a very common weak pattern (e.g., 123, @123, 123!).")

    return issues

