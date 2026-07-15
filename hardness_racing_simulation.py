import random

# =======================================================================
#                               variables
# =======================================================================

horses_list = []
horses = []

# =======================================================================
#                                methods
# =======================================================================


def choose_number_of_horses_and_shuffle_them():
    horses_number = int(input("Indiquez le nombre de chevaux que vous souhaitez voir courir "
                              ": (entre 12 et 20 chevaux) : "))

    while horses_number < 12 or horses_number > 20:
        horses_number = int(input("Vous vous êtes trompés, veuillez réessayer : "))

    list_of_horses = list(range(1, horses_number + 1))
    random.shuffle(list_of_horses)
    return list_of_horses


# ==============================================================
#                           main
# ==============================================================


if __name__ == "__main__":

    print("Bienvenue dans l'hippodrome de Saint-Albe. ")
    choice = input("Voulez-vous jouer à nos course hippique? (O ou N) : ")

    while choice != "O" and choice != "N":
        choice = input("Vous vous êtes trompés, veuillez réessayer : ")

        while choice == "O":
            choose_number_of_horses_and_shuffle_them()
            choice = input("Voulez-vous rejouer? (O ou N) : ")

    print("Nous vous remercions d'avoir jouer dans notre hippodrome. A bientôt ! ")