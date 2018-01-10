def is_pangram(sentence):
    # characters = list(sentence)
    # characters.sort()
    # isogram_characters = []
    #
    # for character in characters:
    #     if character.isalpha():
    #         pass
    #     elif character.upper() in isogram_characters:
    #         pass
    #     isogram_characters.append(character.upper())
    # return False
    characters = list(sentence)
    pangram = []
    for character in characters:
        if character.isalpha() and character not in pangram:
            pangram.append(character.lower())

    temp = 'abcdefghijklmnopqrstuvwxyz'
    pangram.sort()
    pangram = "".join(pangram)
    return pangram == temp

