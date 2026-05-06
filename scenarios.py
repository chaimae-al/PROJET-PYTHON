from data import charger_donnees


def afficher_scenarios():

    data = charger_donnees()

    for scenario in data["scenarios"]:

        print(f"\n===== {scenario['nom']} =====")
        print("Stratégie :", scenario["strategie"])
        print("Étudiants concernés :")

        trouve = False

        for e in data["etudiants"]:

            note = e["note_diagnostique"]

            if note is not None:

                if scenario["min"] <= note <= scenario["max"]:
                    print(
                        e["nom"],
                        "-",
                        note
                    )
                    trouve = True

        if not trouve:
            print("Aucun")