# players.py

# Liste globale de tous les joueurs
joueurs = []

# Créer un joueur humain
def creer_joueur():
    stop = 1
    while stop != 2:
        nom = input("Nom du joueur : ")
        joueur = {
            "nom": nom,
            "type": "humain",  
            "elo": 1000,
            "joues": 0,
            "victoires": 0,
            "defaites": 0,
            "historique": []
        }
        joueurs.append(joueur)
        print(f"Joueur {nom} créé avec succès.")
        print("Ajouter un autre joueur ?")
        print("1. Oui")
        print("2. Non")
        stop = int(input())

# Afficher les joueurs
def afficher_joueurs():
    if not joueurs:
        print("Aucun joueur créé.")
        return
    print("\nListe des joueurs :")
    for i, joueur in enumerate(joueurs):
        print(f"{i+1}. {joueur['nom']} | Victoires : {joueur['victoires']} | Défaites : {joueur['defaites']} | Parties jouées : {joueur['joues']}")
