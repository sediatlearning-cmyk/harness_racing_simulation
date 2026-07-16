import random

# =======================================================================
#                               variables
# =======================================================================

horses_list = []
horses = []
ARTICLE = ", le "
INVALID_INPUT_MESSAGE = "Vous vous êtes trompés, veuillez réessayer : "
speed: int = 0
new_speed: int = 0
distance_traveled: int = 0
disqualification: bool = False
arrival: bool = False
horse: dict = {'speed': speed, 'distance_traveled': distance_traveled,
               'disqualification': disqualification, 'arrival': arrival}
# =======================================================================
#                                methods
# =======================================================================

"""
methode qui traite le type de course (Tiercé, Quarté ou Quinté) en fonction du choix de l'utilisateur

:param horses_list: list_of_horses qui recupere la liste des chevaux
:return: horses_racing_prediction renvoie le choix du type de course par l'utilisateur
"""


def choose_the_type_of_race(list_of_horses):
    print("Choisissez votre genre de course.")
    print("1 pour Tiercé")
    print("2 pour Quarté")
    print("3 pour Quinté")

    horses_racing_prediction = int(input("Quel genre de course souhaitez-vous ? (choix entre 1 et 3) :  "))

    while horses_racing_prediction < 1 or horses_racing_prediction > 3:
        horses_racing_prediction = int(input(INVALID_INPUT_MESSAGE))

    match horses_racing_prediction:
        case 1:
            print("Vous avez choisi le Tiercé.")
            list_of_winners_horses = list_of_horses[:3]
            print("Les chevaux gagnants du Tiercé sont : ")
            print("Le " + str(list_of_winners_horses[0]) + ARTICLE +
                  str(list_of_winners_horses[1]) +
                  " et le " + str(list_of_winners_horses[2]))

        case 2:
            print("Vous avez choisi le Quarté.")
            list_of_winners_horses = list_of_horses[:4]
            print("Les chevaux gagnants du Quarté sont : ")
            print("Le " + str(list_of_winners_horses[0]) + ARTICLE +
                  str(list_of_winners_horses[1]) + ARTICLE +
                  str(list_of_winners_horses[2])
                  + " et le " + str(list_of_winners_horses[3]))

        case 3:
            print("Vous avez choisi le Quinté.")
            list_of_winners_horses = list_of_horses[:5]
            print("Les chevaux gagnants du Quinté sont : ")
            print("Le " + str(list_of_winners_horses[0]) + ARTICLE +
                  str(list_of_winners_horses[1]) + ARTICLE +
                  str(list_of_winners_horses[2]) +
                  ARTICLE + str(list_of_winners_horses[3]) + " , le " + str(list_of_winners_horses[4]))


"""
méthode qui traite le nombre de chevaux choisis par l'utilisateur et qui les mélange 
afin qu'il soit dans un ordre aléatoire

:return: list_of_horses renvoie une liste avec l'ordre des chevaux préalablement mélangé 
"""


def choose_number_of_horses_and_shuffle_them():
    horses_number = int(input("Indiquez le nombre de chevaux que vous souhaitez voir courir "
                              ": (entre 12 et 20 chevaux) : "))

    while horses_number < 12 or horses_number > 20:
        horses_number = int(input(INVALID_INPUT_MESSAGE))

    list_of_horses = list(range(1, horses_number + 1))
    random.shuffle(list_of_horses)
    return list_of_horses


"""
Méthode qui traite l'ensemble des méthodes dans un ordre définis afin 
d'obtenir les résultats d'arrivées des chevaux par le type de course choisi 
"""


def result_calculated():

    list_of_horses = choose_number_of_horses_and_shuffle_them()

    choose_the_type_of_race(list_of_horses)

# ==============================================================
#                           main
# ==============================================================


if __name__ == "__main__":

    print("Bienvenue dans l'hippodrome de Saint-Albe. ")
    choice = input("Voulez-vous jouer à nos course hippique? (O ou N) : ")

    while choice != "O" and choice != "N":
        choice = input(INVALID_INPUT_MESSAGE)

        while choice == "O":
            result_calculated()
            choice = input("Voulez-vous rejouer? (O ou N) : ")

    print("Nous vous remercions d'avoir jouer dans notre hippodrome. A bientôt ! ")