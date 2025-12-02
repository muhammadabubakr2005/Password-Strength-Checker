from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from password_checker.dictionary_check import load_dictionary
from password_checker.strength_meter import evaluate_password

app = FastAPI()
dictionary = load_dictionary("dictionaries/common_passwords.txt")

# --- CORS Fix ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PasswordInput(BaseModel):
    password: str

@app.post("/check")
def check_password(data: PasswordInput):
    return evaluate_password(data.password, dictionary)
