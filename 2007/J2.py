def main():

    while True:
        short_form = input("Enter phrase> ")

        if short_form == "CU":
            print("see you")
        elif short_form == ":-)":
            print("I'm happy")
        elif short_form == ":-(":
            print("I'm unhappy")
        elif short_form == ";-)":
            print("wink")
        elif short_form == ":-P":
            print("stick out my tongue")
        elif short_form == "(~.~)":
            print("sleepy")
        elif short_form == "TA":
            print("totally awesome")
        elif short_form == "CCC":
            print("Canadian Computing-Competition")
        elif short_form == "CUS":
            print("because")
        elif short_form == "TW":
            print("thank-you")
        elif short_form == "YW":
            print("you're welcome")
        elif short_form == "TTYL":
            print("talk to you later")
            break
        else:
            print(f"{short_form}")


main()
