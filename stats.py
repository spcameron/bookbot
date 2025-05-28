def count_words(str):
    words = str.split()
    return len(words)

def count_characters(str):
    characters = {}
    words = str.split()
    for word in words:
        for character in word:
            character = character.lower()
            if character not in characters:
                characters[character] = 0
            characters[character] += 1
    return characters

def sort_character_counts(dict):
    ordered_list = []
    for key, value in dict.items():
        entry = {}
        entry["char"] = key
        entry["num"] = value
        ordered_list.append(entry)
    ordered_list.sort(reverse=True, key=sort_on)
    return ordered_list

def sort_on(dict):
    return dict["num"]