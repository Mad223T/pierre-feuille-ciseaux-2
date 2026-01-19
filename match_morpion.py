from players import joueurs

def jouer_match_morpion():
    if len(joueurs) < 2:
        print("Il faut au moins 2 joueurs.")
        return

    grille = [" "] * 9
    joueur_actuel = "X"
    noms = [joueurs[0]["nom"], joueurs[1]["nom"]]

    def afficher_grille():
        print("\n")
        print(f" {grille[0]} | {grille[1]} | {grille[2]} ")
        print("---|---|---")
        print(f" {grille[3]} | {grille[4]} | {grille[5]} ")
        print("---|---|---")
        print(f" {grille[6]} | {grille[7]} | {grille[8]} ")
        print("\n")

    while True:
        afficher_grille()
        try:
            case = int(input(f"{noms[0 if joueur_actuel=='X' else 1]}, choisis une case (1-9) : ")) - 1
        except ValueError:
            print("Choix invalide.")
            continue

        if case < 0 or case > 8 or grille[case] != " ":
            print("Case invalide ou déjà prise.")
            continue

        grille[case] = joueur_actuel

        lignes = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        victoire = False
        for l in lignes:
            if grille[l[0]] == grille[l[1]] == grille[l[2]] != " ":
                afficher_grille()
                print("\n==============================")
                print("          GREAT GAME")
                print("==============================")
                print(f"Le gagnant est : {noms[0 if joueur_actuel=='X' else 1]}")
                print("==============================\n")
                victoire = True
                break

        if victoire:
            return

        if " " not in grille:
            afficher_grille()
            print("\n==============================")
            print("          GREAT GAME")
            print("==============================")
            print("Égalité !")
            print("==============================\n")
            return

        joueur_actuel = "O" if joueur_actuel=="X" else "X"