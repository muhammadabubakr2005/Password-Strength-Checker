from password_checker.dictionary_check import load_dictionary
from password_checker.strength_meter import evaluate_password

DICT_PATH = "dictionaries/common_passwords.txt"

def main():
    dictionary = load_dictionary(DICT_PATH)

    print("=== Password Strength Checker ===")
    pwd = input("Enter password: ")

    result = evaluate_password(pwd, dictionary)

    print("\n[RESULT]")
    print("Strength:", result["category"])
    print("Score:", result["score"])
    print("---- Details ----")
    for item in result["details"]:
        print(item)

if __name__ == "__main__":
    main()
