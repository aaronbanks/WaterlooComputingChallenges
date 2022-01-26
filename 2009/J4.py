def main():

    sign_message = "WELCOME TO CCC GOOD LUCK TODAY"
    sign_words = sign_message.split()

    length_of_signage = int(input("Enter w:"))

    final_print = ""

    while True:
        words_on_current_line = []
        space_remaining_on_line = length_of_signage
        first_word_on_line = True
        blank_space = 0

        for word in sign_words:

            if first_word_on_line == True:
                words_on_current_line.append(word)
                space_remaining_on_line -= len(word)
                first_word_on_line = False
                print("ERROR CHECK: FIRST WORD")

            else:
                if len(word) + 1 <= space_remaining_on_line:
                    words_on_current_line.append(word)
                    space_remaining_on_line -= len(word) + 1
                    blank_space += 1
                    print("ERROR CHECK: NON FIRST WORD ")


                else:
                    if len(words_on_current_line) == 1:
                        final_print += (
                            words_on_current_line[0]
                            + (space_remaining_on_line * ".")
                            + "\n"
                        )
                        print("ERROR CHECK: ONE WORD ON LINE")

                    else:
                        space_size = int(
                            (space_remaining_on_line + blank_space)
                            / (len(words_on_current_line) - 1)
                        )
                        extra_spaces = space_remaining_on_line % (
                            len(words_on_current_line) - 1
                        )
                        print("ERROR CHECK: MULTI WORDS ON LINE 1")

                        for wordd in words_on_current_line:
                            if extra_spaces > 0:
                                extra_spaces -= 1
                                final_print += ("." * (space_size + 1)) + wordd
                            else:
                                final_print += ("." * space_size) + wordd
                        final_print += "\n"
                        print("ERROR CHECK: MULTI WORDS ON LINE 2")

                    for words in words_on_current_line:
                        sign_words.remove(words)

        if len(sign_words) == 0:
            break

    print(final_print)


main()
