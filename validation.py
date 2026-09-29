def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def get_choice(message, minimum, maximum):
    while True:
        try:
            value = int(input(message))

            if minimum <= value <= maximum:
                return value
            else:
                print(
                    "Please enter a number between",
                    minimum,
                    "and",
                    maximum
                )

        except ValueError:
            print("Please enter a valid number.")