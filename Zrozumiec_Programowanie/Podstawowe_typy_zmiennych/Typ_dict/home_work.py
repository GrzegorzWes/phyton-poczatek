# Zadanie nr 2
# Stwórz zmienną my_family zawierającą drzewo genealogiczne Twojej rodziny.
#
# Zacznij od siebie, opisując imię, nazwisko oraz datę urodzenia każdej osoby oraz jej rodziców.
#
# Podpowiedź: rodzice będą listami zawierającymi w sobie kolejne słowniki.

my_family = {
    "first_name": "Grzegorz",
    "last_name": "Wesołowski",
    "date_of_brith": "11-02-1986",
    "parents": [
        {
            "first_name": "Krzysztof",
            "last_name": "Wesołowski",
            "date_of_birth": "15-11-1961",
            "parents":  [
                {
                    "first_name": "Stefan",
                    "last_name": "Wesołowski",
                    "date_of_birth": "12-08-1920",
                    "parents": [],
                },
                [
                    {
                        "first_name": "Janina"
                    }
                ]
            ]

        }

    ]
}