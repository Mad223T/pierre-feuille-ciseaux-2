from players import joueurs, creer_joueur, afficher_joueurs
from Tournoi import creer_tournoi
import match_morpion
import match_ppc

# ------------------------------
# Tournoi / stats              |
# ------------------------------

def reprendre_tournoi():
    print("Reprendre tournoi (squelette)")

def historique_tournoi():
    print("Historique tournoi (squelette)")

def classement_elo():
    if not joueurs:
        print("Aucun joueur créé.")
        return
    joueurs_tries = sorted(joueurs, key=lambda j: j['elo'], reverse=True)
    print("\n==============================")
    print("        CLASSEMENT ELO")
    print("==============================")
    print(f"{'Nom':<15} {'ELO':<6} {'Victoires':<9} {'Défaites':<8}")
    print("------------------------------")
    for j in joueurs_tries:
        print(f"{j['nom']:<15} {j['elo']:<6} {j['victoires']:<9} {j['defaites']:<8}")
    print("==============================\n")

def stats_joueur():
    afficher_joueurs()

def afficher_regles():
    print("\n==============================")
    print("          RÈGLES DU JEU")
    print("==============================")
    print("Le joueur doit effectuer des parties stratégiques liées au principe du jeu.")
    print("Il se doit de remporter trois manches pour gagner le match.")
    print("Chaque action peut avoir un impact positif ou négatif sur le déroulement de la partie.")
    print("Le match se terminera lorsque les conditions de victoires ou défaites ont été atteintes.")
    print("==============================\n")

# ------------------------------
# Menu principal               |
# ------------------------------

def afficher_menu():
    print("\n" + "="*40)
    print(" " * 15 + "JANKEN")
    print("="*40)
    print("1. Creer un joueur")
    print("2. Creer un tournoi")
    print("3. Reprendre un tournoi")
    print("4. Historique")
    print("5. Classement ELO")
    print("6. Statistiques joueur")
    print("7. Regles")
    print("8. Jouer PPC")
    print("9. Jouer Morpion")
    print("10. Quitter") 

def main():
    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            creer_joueur()
        elif choix == "2":
            tournoi = creer_tournoi()
            if tournoi:
                print(f"Tournoi '{tournoi['nom']}' créé et prêt pour le tournoi !")
        elif choix == "3":
            reprendre_tournoi()
        elif choix == "4":
            historique_tournoi()
        elif choix == "5":
            classement_elo()
        elif choix == "6":
            stats_joueur()
        elif choix == "7":
            afficher_regles()
        elif choix == "8":
            match_ppc.jouer_match_ppc()
        elif choix == "9":
            match_morpion.jouer_match_morpion()
        elif choix == "10":
            print("Au revoir ")
            break
        else:
            print("Choix invalide, réessaye")

if __name__ == "__main__":
    main()
