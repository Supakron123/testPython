def is_isogram(string):
    characters = list(string)
    isogram_characters = []
    print(f'Characters: {characters}')
    for character in characters:
        if character == '-' or character == ' ':
            pass
        elif character.upper() in isogram_characters:
            return False
        isogram_characters.append(character.upper())

    return True