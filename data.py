
# ============================
# DATA
# ============================
{
"etudiants": [],
"scenarios": [
    {"id":1,"nom":"Remédiation","min":0,"max":5,"strategie":"Révision et tutorat"},
    {"id":2,"nom":"Consolidation","min":6,"max":7,"strategie":"Exercices d'application"},
    {"id":3,"nom":"Investissement","min":8,"max":10,"strategie":"Mini-projets"}
]
}

import json
import os

FICHIER = "database.json"


# ============================
#  Charger les données
# ============================
def charger_donnees():
    if not os.path.exists(FICHIER):
        return initialiser_donnees()

    try:
        with open(FICHIER, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        print("⚠️ Erreur lecture fichier, réinitialisation...")
        return initialiser_donnees()


# ============================
#  Sauvegarder les données
# ============================
def sauvegarder_donnees(data):
    try:
        with open(FICHIER, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except:
        print("❌ Erreur lors de la sauvegarde")


# ============================
#Initialisation automatique
# ============================
def initialiser_donnees():
    data = {
        "etudiants": [],
        "scenarios": [
            {"id":1,"nom":"Remédiation","min":0,"max":5,"strategie":"Révision et tutorat"},
            {"id":2,"nom":"Consolidation","min":6,"max":7,"strategie":"Exercices d'application"},
            {"id":3,"nom":"Investissement","min":8,"max":10,"strategie":"Mini-projets"}
        ]
    }

    sauvegarder_donnees(data)
    return data


# ============================
# Fonction utilitaire
# ============================
def reinitialiser_base():
    confirmation = input("⚠️ Réinitialiser la base ? (oui/non) : ")

    if confirmation.lower() == "oui":
        data = initialiser_donnees()
        print("✅ Base réinitialisée")
        return data

    print("❌ Annulé")