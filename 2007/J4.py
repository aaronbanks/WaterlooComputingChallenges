def main():

    first_phrase = input("Enter first phrase> ")
    second_phrase = input("Enter second phrase> ")

    first_phrase_letters = []
    second_phrase_letters = []

    for letter in first_phrase:
        if letter == " ":
            continue
        first_phrase_letters.append(letter)

    for letter in second_phrase:
        if letter == " ":
            continue
        second_phrase_letters.append(letter)

    if sorted(first_phrase_letters) == sorted(second_phrase_letters):
        print("Is an anagram")
    else:
        print("Is not an anagram")


main()
