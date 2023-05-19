'''
projekt_1.py: První projekt do Engeto Online Python Akademie

author = Petr Kulig
email: petrkg@centrum.cz
discord> Petr Kulig#4490
'''


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]





users = {"bob": "123", "ann": "pass123","mike": "password123","liz": "pass123"}

access = input("Zadej svoje jemno: ")
paa_word = input("Zadej svoje heslo: ")

if access in users:

    if users[access] == paa_word:

        print("Welcome to the app, ", access)
        print("We have 3 texts to be analyzed.")
        print("First text", TEXTS[0] + '\n', "Second text\n", TEXTS[1] + '\n', "Third text\n", TEXTS[2])
        print(30* "-")
        choose = input("Please choose the text and use 1,2,3: ")
        print(30 * "-")
        choose = int(choose)
        if choose in [1,2,3]:
            chosen_text = TEXTS[choose -1]
            new_text1 = chosen_text.split()
            count_word = len(new_text1)
            title_word = sum(1 for word in new_text1 if word.istitle())
            upper_word = sum(1 for word in new_text1 if word.isupper())
            lower_word = sum(1 for word in new_text1 if word.islower())
            numeric_word = sum(1 for word in new_text1 if word.isnumeric())
            count_word1 = [int(word) for word in new_text1 if word.isdigit()]
            total_sum = sum(count_word1)


            print("There are", count_word, "words in seleted text")
            print("There are", title_word, "words with titlecase")
            print("There are", upper_word, "words in seleted text")
            print("There are", lower_word, "words in seleted text")
            print("There are", numeric_word, "words in seleted text")
            print(total_sum)

            new_tab = {}
            for word in new_text1:
                length = len(word)
                if length in new_tab:
                    new_tab[length] += 1
                else:
                    new_tab[length] = 1

            max_count = max(new_tab.values())

            for length in range(1, max_count + 1):
                count = new_tab.get(length, 0)
                print(f"{length:2}| {'*' * count:12} {count}")
        else:
            print("You have to choose only from 1,2 or 3")
    else:
        print("This is not correct user name or password")
else:
    print("This is not correct user name or password")

