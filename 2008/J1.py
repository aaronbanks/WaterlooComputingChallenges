def main():

    weight = float(input("Enter weight: "))

    height = float(input("Enter height: "))

    bmi = weight / (height * height)

    if bmi > 25:
        print("Overweight")
    elif bmi < 18.5:
        print("Underweight")
    else:
        print("Normal weight")


main()
