ingredient1 = "pasta"
ingredient2 = "meatballs"

if ingredient1 == "pasta":
    if ingredient2 == "meatballs":
        print("pasta and meatballs")
    else:
        print("plain pasta")
else:
    print("no recomendation")

if ingredient1 == "pasta" and ingredient2 == "meatballs":
    print("pasta and meatballs")
elif ingredient1 == "pasta":
    print("plain pasta")
else:
    print("no recomendation")