# Règles du jeu : Simulateur de course de trot attelé

## Objectif

Simuler une course de trot attelé entre plusieurs chevaux sur une piste de **2 400 mètres**.

Au début de la partie, l'utilisateur choisit :

- le **nombre de chevaux** (entre **12 et 20**),
- le **type de course** :
  - **Tiercé** : afficher les **3 premiers** à l'arrivée,
  - **Quarté** : afficher les **4 premiers**,
  - **Quinté** : afficher les **5 premiers**.

---

## État initial

Au départ, chaque cheval possède les caractéristiques suivantes :

- **Vitesse :** 0
- **Distance parcourue :** 0 m
- **Statut :** en course

Tous les chevaux commencent **à l'arrêt**.

---

## Déroulement d'un tour

Chaque tour représente **10 secondes** de course.

Pour **chaque cheval encore en course**, les étapes suivantes sont exécutées :

1. Lancer un dé à **6 faces**.
2. Modifier la vitesse du cheval selon le tableau d'évolution des vitesses.
3. Si le résultat est **DQ**, le cheval est **disqualifié**.
4. Sinon, le cheval avance de la distance correspondant à sa nouvelle vitesse.

Une fois tous les chevaux traités, le programme peut afficher :

- la vitesse de chaque cheval,
- la distance parcourue,
- les éventuelles disqualifications.

L'utilisateur lance ensuite le tour suivant.

---

## Évolution de la vitesse

La variation de la vitesse dépend :

- de la **vitesse actuelle** du cheval,
- du **résultat du dé**.

| Vitesse actuelle | Dé = 1 | Dé = 2 | Dé = 3 | Dé = 4 | Dé = 5 | Dé = 6 |
|-----------------:|:------:|:------:|:------:|:------:|:------:|:------:|
| 0 | 0 | +1 | +1 | +1 | +2 | +2 |
| 1 | 0 | 0 | +1 | +1 | +1 | +2 |
| 2 | 0 | 0 | +1 | +1 | +1 | +2 |
| 3 | -1 | 0 | 0 | +1 | +1 | +1 |
| 4 | -1 | 0 | 0 | 0 | +1 | +1 |
| 5 | -2 | -1 | 0 | 0 | 0 | +1 |
| 6 | -2 | -1 | 0 | 0 | 0 | DQ |

**Remarque :**

- `+1` signifie que la vitesse augmente de 1.
- `-1` signifie que la vitesse diminue de 1.
- `0` signifie que la vitesse reste identique.
- `DQ` signifie que le cheval est **disqualifié** et quitte définitivement la course.

---

## Distance parcourue

Après la mise à jour de la vitesse, le cheval avance selon le tableau suivant :

| Vitesse | Distance parcourue (m) |
|---------:|-----------------------:|
| 0 | 0 |
| 1 | 23 |
| 2 | 46 |
| 3 | 69 |
| 4 | 92 |
| 5 | 115 |
| 6 | 138 |

---

## Arrivée

Un cheval est considéré comme arrivé lorsque sa distance parcourue est **supérieure ou égale à 2 400 mètres**.

Son ordre d'arrivée est alors enregistré.

Les chevaux arrivés ne jouent plus les tours suivants.

---

## Fin de la course

La course se termine lorsque **tous les chevaux non disqualifiés** ont franchi la ligne d'arrivée.

Les chevaux disqualifiés ne sont pas classés.

---

## Résultat final

À la fin de la simulation, seuls les premiers chevaux correspondant au type de course sont affichés :

- **Tiercé** → les **3 premiers**
- **Quarté** → les **4 premiers**
- **Quinté** → les **5 premiers**
