from data import charger_donnees, sauvegarder_donnees


# ============================
# ➕ Ajouter étudiant
# ============================
def ajouter_etudiant():
    data = charger_donnees()

    matricule = input("Matricule : ")
    nom = input("Nom : ")
    niveau = input("Niveau : ")

    # Vérification doublon
    for e in data["etudiants"]:
        if e["matricule"] == matricule:
            print("❌ Étudiant déjà existant")
            return

    etudiant = {
        "matricule": matricule,
        "nom": nom,
        "niveau": niveau,
        "note_diagnostique": None,
        "note_formative": None
    }

    data["etudiants"].append(etudiant)
    sauvegarder_donnees(data)

    print("✅ Étudiant ajouté avec succès")


# ============================
# ❌ Supprimer étudiant
# ============================
def supprimer_etudiant():
    data = charger_donnees()

    matricule = input("Matricule à supprimer : ")

    for e in data["etudiants"]:
        if e["matricule"] == matricule:
            data["etudiants"].remove(e)
            sauvegarder_donnees(data)
            print("✅ Étudiant supprimé")
            return

    print("❌ Étudiant introuvable")


# ============================
# 📋 Afficher étudiants
# ============================
def afficher_etudiants():
    data = charger_donnees()

    if not data["etudiants"]:
        print("⚠️ Aucun étudiant enregistré")
        return

    print("\n===== LISTE DES ÉTUDIANTS =====")

    for e in data["etudiants"]:
        print(f"""
Matricule : {e['matricule']}
Nom       : {e['nom']}
Niveau    : {e['niveau']}
Diagnostique : {e['note_diagnostique']}
Formative    : {e['note_formative']}
------------------------------
""")


# ============================
# ✏️ Ajouter note diagnostique
# ============================
def ajouter_note_diagnostique():
    data = charger_donnees()

    matricule = input("Matricule : ")

    for e in data["etudiants"]:
        if e["matricule"] == matricule:

            try:
                note = float(input("Note diagnostique (0-10) : "))
            except:
                print("❌ Valeur invalide")
                return

            if not (0 <= note <= 10):
                print("❌ La note doit être entre 0 et 10")
                return

            e["note_diagnostique"] = note
            sauvegarder_donnees(data)

            print("✅ Note diagnostique enregistrée")
            return

    print("❌ Étudiant introuvable")


# ============================
# ✏️ Ajouter note formative
# ============================
def ajouter_note_formative():
    data = charger_donnees()

    matricule = input("Matricule : ")

    for e in data["etudiants"]:
        if e["matricule"] == matricule:

            try:
                note = float(input("Note formative (0-10) : "))
            except:
                print("❌ Valeur invalide")
                return

            if not (0 <= note <= 10):
                print("❌ La note doit être entre 0 et 10")
                return

            e["note_formative"] = note
            sauvegarder_donnees(data)

            print("✅ Note formative enregistrée")
            return

    print("❌ Étudiant introuvable")