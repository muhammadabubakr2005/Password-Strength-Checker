from .entropy import calculate_entropy
from .dictionary_check import is_common_password
from .patterns import detect_patterns

def evaluate_password(password: str, dictionary: set):
    report = []
    score = 0

    length = len(password)
    entropy = calculate_entropy(password)
    patterns = detect_patterns(password)
    dictionary_hit = is_common_password(password, dictionary)

    # -----------------------------------------------------------
    # 1) Entropy Scoring (40 points)
    # -----------------------------------------------------------
    report.append(f"Entropy: {entropy} bits")

    if entropy < 28:
        score += 5
    elif entropy < 36:
        score += 10
    elif entropy < 60:
        score += 20
    elif entropy < 80:
        score += 30
    else:
        score += 40

    # -----------------------------------------------------------
    # 2) Length Scoring (30 points)
    # -----------------------------------------------------------
    if length < 8:
        report.append("❌ Too short (<8 characters)")
        score += 0
    elif length < 12:
        report.append("⚠️ Minimum acceptable length (8–11)")
        score += 10
    elif length < 16:
        report.append("✅ Good length (12–15)")
        score += 20
    else:
        report.append("🔥 Excellent length (16+)")
        score += 30

    # -----------------------------------------------------------
    # 3) Character Variety (20 points)
    # -----------------------------------------------------------
    variety_score = 0
    if any(c.islower() for c in password): variety_score += 1
    if any(c.isupper() for c in password): variety_score += 1
    if any(c.isdigit() for c in password): variety_score += 1
    if any(not c.isalnum() for c in password): variety_score += 1

    score += variety_score * 5

    if variety_score == 4:
        report.append("🔥 Excellent variety (lowercase, uppercase, digits, symbols)")
    elif variety_score == 3:
        report.append("✅ Good variety")
    elif variety_score == 2:
        report.append("⚠️ Weak variety")
    else:
        report.append("❌ Very poor variety (use mixed characters)")

    # -----------------------------------------------------------
    # 4) Dictionary penalties (−20 points)
    # -----------------------------------------------------------
    if dictionary_hit:
        report.append("❌ Appears in common password dictionary")
        score -= 20

    # -----------------------------------------------------------
    # 5) Pattern penalties (−10 each, up to −30 max)
    # -----------------------------------------------------------
    if patterns:
        for p in patterns[:3]:
            report.append("⚠️ " + p)
            score -= 10

    # -----------------------------------------------------------
    # Final Score Normalization (0–100)
    # -----------------------------------------------------------
    score = max(0, min(score, 100))

    if score < 25:
        category = "VERY WEAK"
    elif score < 50:
        category = "WEAK"
    elif score < 70:
        category = "MEDIUM"
    elif score < 85:
        category = "STRONG"
    else:
        category = "VERY STRONG"

    return {
        "password": password,
        "score": score,
        "category": category,
        "details": report
    }
