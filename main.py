from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "super_secret_key"

provocari_normal = [
    "Fă 10 flotări 💪",
    "Cântă 30 secunde 🎤",
    "Imită un animal 🐒",
    "Spune un banc 😆",
    "Dansează 1 minut 💃"
]

provocari_18 = [
    "Spune cel mai mare secret 😏",
    "Trimite un mesaj random cuiva 😈",
    "Alege pe cineva să bea un shot 🍻",
    "Spune pe cine ai plăcea din cameră 🔥",
    "Adevăr sau provocare (hard mode) 😜"
]

@app.route("/")
def index():
    mod = request.args.get("mod", "normal")

    if mod == "18":
        provocari = provocari_18
    else:
        provocari = provocari_normal

    if "istoric" not in session:
        session["istoric"] = []

    disponibile = [p for p in provocari if p not in session["istoric"]]

    if not disponibile:
        session["istoric"] = []
        disponibile = provocari

    provocare = random.choice(disponibile)
    session["istoric"].append(provocare)

    return render_template("index.html", provocare=provocare, mod=mod)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
