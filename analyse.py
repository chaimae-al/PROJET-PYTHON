# from data import charger_donnees


def analyser_impact():

    data = charger_donnees()

    print("\n===== ANALYSE D'IMPACT =====")

    for e in data["etudiants"]:

        diag = e["note_diagnostique"]
        form = e["note_formative"]

        if diag is None or form is None:
            continue

        progression = form - diag

        print(f"\n{e['nom']}")

        if progression >= 3:
            print("Impact très fort")

        elif progression >= 1:
            print("Impact positif")

        elif progression == 0:
            print("Impact neutre")

        else:
            print("Impact négatif")