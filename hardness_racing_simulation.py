
# =======================================================================
#                               variables
# =======================================================================


# =======================================================================
#                                methods
# =======================================================================


# ==============================================================
#                           main
# ==============================================================


if __name__ == "__main__":

    print("Bienvenue dans l'hippodrome de Saint-Albe. ")
    choice = input("Voulez-vous jouer à nos course hippique? (O ou N) : ")

    while choice != "O" and choice != "N":
        choice = input("Vous vous êtes trompés, veuillez réessayer : ")

        while choice == "O":
            choice = input("Voulez-vous rejouer? (O ou N) : ")

    print("Nous vous remercions d'avoir jouer dans notre hippodrome. A bientôt ! ")