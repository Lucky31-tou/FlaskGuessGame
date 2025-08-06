from flask import Flask, render_template, request, redirect, url_for, session
from random import randint

app = Flask(__name__)
app.secret_key = "1bf6aa7ec10e40edcd99a10b394b3194a3d67e4c3f2b2fda80d3be6696df5dc7"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/jeu", methods=["POST", "GET"])
def jeu():
    if request.method == "POST":
        # Traiter les données 
        reponse = int(request.form.get("nombre"))
        session["tent"].append(reponse)
        if reponse == session["nb"]:
            session["en_cours"] = False
            message = "C'est gagné !"
        elif reponse < session["nb"]:
            message = "C'est plus"
        else:
            message = "C'est moins"
        session["essai"] -= 1

        if session['essai'] == 0:
            session["en_cours"] = False
            message = "C'est perdu !"
        return render_template("nb_mystere.html", message=message)
    else:
        nb_mys = randint(0, 100)
        session["nb"] = nb_mys
        session["en_cours"] = True
        session["essai"] = 10
        session["tent"] = []
        # Afficher le formulaire
        return render_template("nb_mystere.html")
    

users = [
    {"nom" : "admin", "mdp" : "1234"},
    {"nom" : "marie", "mdp" : "nsi"},
    {"nom" : "paul", "mdp" : "azerty"}
]

def recherche_user(nom, mdp):
    for user in users:
        if user['nom'] == nom and user["mdp"] == mdp:
            return user
    return None

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        donnees = request.form
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')
        
        user = recherche_user(nom, mdp)
        if user is not None:
            session["nom_user"] = user["nom"]
            return redirect(url_for("index"))
        else:
            return redirect(request.url)
    else:
        if "nom_user" in session:
            return redirect(url_for("index"))
        return render_template("formulaires.html")
    

@app.route("/logout")
def logout():
    session.pop("nom_user", None)
    return redirect(url_for('login'))


@app.route("/compteur")
def compteur():
    if "compteur" not in session:
        session["compteur"] = 1
    else:session["compteur"] += 1
    nb_visit = session["compteur"]
    return f"Vous avez visité cette page {nb_visit} fois"



if __name__=="__main__":
    app.run(debug=True)