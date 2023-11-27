def extraire_nom_president(nom_fichier):
    nom_fichier = nom_fichier.replace("Nomination_", "").replace(".txt", "")

    elements = nom_fichier.rsplit("(", 1)

    nom_president = elements[0].strip()

    nom_president = ''.join([char for char in nom_president if not char.isdigit()])

    return nom_president

def associer_prenom_a_president(nom_president):
    prenoms = {
        "Chirac": "Jacques",
        "Giscard dEstaing": "Valéry",
        "Hollande": "François",
        "Macron": "Emmanuel",
        "Mitterrand": "François",
        "Sarkozy": "Nicolas"
        # Ajoutez d'autres présidents au besoin
    }

    # Trouver le dernier mot dans le nom du président
    mots = nom_president.split(" ")
    nom_famille = mots[-1]

    # Vérifier si le nom de famille est dans le dictionnaire
    if nom_famille in prenoms:
        prenom = prenoms[nom_famille]
    else:
        prenom = "Prénom non trouvé"

    return prenom



