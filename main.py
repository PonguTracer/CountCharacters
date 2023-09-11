def count_character_in_phrase(character, phrase):
    count = phrase.count(character)
    return f"{count} {character}'s" if count != 1 else f"{count} {character}"


# Input
input_string = input("Enter a character and a phrase: ")

# Split the input into character and phrase
parts = input_string.split()

if len(parts) != 2:
    print("Invalid input format")
else:
    character, phrase = parts
    result = count_character_in_phrase(character, phrase)
    print(result)
