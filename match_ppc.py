import getpass
import random
from players import joueurs

def demander_choix(nom_joueur):
    """Demande le choix d'un joueur (p/f/c), caché à l'écran"""
    correspondance = {"p": "pierre", "f": "feuille", "c": "ciseaux"}
    while True:
        choix = getpass.getpass(f"{nom_joueur}, choisis [p] / [f] / [c] : ").lower()
        if choix in correspondance:
            return correspondance[choix]
        print("Choix invalide. Tape p, f ou c.")

def jouer_match_ppc():
    if len(joueurs) < 2:
        print("Il faut au moins 2 joueurs pour jouer.")
        return

    print("***** Choisissez les joueurs *****")
    for i, joueur in enumerate(joueurs):
        print(f"{i+1}. {joueur['nom']}")

    n = random.choice(joueurs)
    print(n)

    print(demander_choix(joueurs[1]))


    