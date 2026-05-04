# from etudiants import *
# from scenarios import afficher_scenarios
# from analyse import analyser_impact
# from evaluations import statistiques


def menu():

    while True:

        print("""
===== IMPACT DES PRATIQUES SUR LES APPRENTISSAGES =====

1. Ajouter étudiant
2. Supprimer étudiant
3. Afficher étudiants
4. Ajouter note diagnostique
5. Ajouter note formative
6. Afficher scénarios
7. Analyser impact
8. Statistiques
9. Quitter
        """)

        choix = input("Choix : ")

        if choix == "1":
            # ajouter_etudiant()
            pass
        elif choix == "2":
            # supprimer_etudiant()
            pass    
        elif choix == "3":
            # afficher_etudiants()
            pass
        elif choix == "4":
            # ajouter_note("note_diagnostique")
            pass
        elif choix == "5":
            # ajouter_note("note_formative")
            pass
        elif choix == "6":
            # afficher_scenarios()
            pass

        elif choix == "7":
            # analyser_impact()
            pass

        elif choix == "8":
            # statistiques()
            pass

        elif choix == "9":
            break


menu()