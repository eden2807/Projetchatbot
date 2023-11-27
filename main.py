from fonction_noms_présidents import extraire_nom_president, associer_prenom_a_president
fichiers = [
    "Nomination_Chirac1.txt",
    "Nomination_Chirac2.txt",
    "Nomination_Giscard dEstaing.txt",
    "Nomination_Hollande.txt",
    "Nomination_Macron(1).txt",
    "Nomination_Mitterrand1.txt",
    "Nomination_Mitterrand2.txt",
    "Nomination_Sarkozy(1).txt"
]

for fichier in fichiers:
    nom_president = extraire_nom_president(fichier)
    print(f"Nom du président dans '{fichier}': {nom_president}")

noms_presidents = [
    "Chirac",
    "Giscard dEstaing",
    "Hollande",
    "Macron",
    "Mitterrand",
    "Sarkozy"
]

for nom_president in noms_presidents:
    prenom = associer_prenom_a_president(nom_president)
    print(f"Prénom associé à {nom_president}: {prenom}")