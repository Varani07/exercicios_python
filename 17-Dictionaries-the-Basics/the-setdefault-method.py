film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Michael Bay",
    "Goodfellas": "Martin Scorsese"
}

print(film_directors.get("Goodfellas"))
print(film_directors.get("Bad Boys", "Michael Bay"))
print()
print(film_directors)

print()

film_directors.setdefault("Bad Boys", "Michael Bay")
print(film_directors)

print()
film_directors.setdefault("Bad Boys", "A Good Director")
print(film_directors)

print()
film_directors.setdefault("She Said")
print(film_directors)

# =======================================================================

def to_dictionary(list_of_str):
    new_dict = {}
    for num, string in enumerate(list_of_str):
        new_dict[string] = num
    return new_dict
    
print(to_dictionary(["here", "we", "are"]))

# MEU CÓDIGO
def length_counts(list_of_strings):
    new_dict = {}
    for string in list_of_strings:
        lenght = len(string)
        if lenght in new_dict:
            new_dict[lenght] += 1
        else:
            new_dict[lenght] = 1
    return new_dict

# PROFESSOR
def length_counts_prof(elements):
    counts = {}

    for element in elements:
        length = len(element)
        current_count = counts.get(length, 0)
        counts[length] = current_count + 1
    return counts

print()
print(length_counts_prof(["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]))