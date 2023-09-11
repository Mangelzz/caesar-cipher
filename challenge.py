from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
    , 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v' , 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(text, shift, direction):
    end_text = ""
    if direction == 'decode':
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction}d text is: {end_text}")


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

print(logo)
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift >= 45:
        shift = shift % 26
    caesar(text, shift, direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if result == 'no':
        should_continue = False
        print("Goodbye")