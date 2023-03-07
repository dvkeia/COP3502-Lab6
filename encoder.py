# Encoder function
def encode(password):
    encoded = ""
    for val in password:
        num = int(val)
        num = num + 3
        # Ensures num remains one digit
        num = num % 10
        encoded = encoded + str(num)
    return encoded


def main():
    choice = -1
    password = ""

    # While loop to keep encoding and decoding password as necessary
    while True:
        print("Menu")
        print("------------")
        print("1. Encode\n2. Decode\n3. Quit")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        # To be implemented after programming partner adds decoder function
        elif choice == 2:
            pass
        elif choice == 3:
            break


if __name__ == "__main__":
    main()